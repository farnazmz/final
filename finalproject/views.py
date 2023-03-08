import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from datetime import *
from django.utils import timezone
from .forms import NoteForm, BedtimeForm, NutritionForm
from .models import User, Note, Sleep, Nutrition


# returning the home page
@csrf_exempt
def index(request):
    return render(request, "finalproject/index.html")


# all memos will be shown only to the signed in
# authenticated user with the option to modify with json
@csrf_exempt
def memo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid():
                note = Note(
                    this_user=request.user,
                    note_date=timezone.now(),
                    my_note=form.cleaned_data["my_note"]
                )
                note.save()
            return redirect("memo")
        else:
            memos= Note.objects.all().order_by("-note_date")
            
            return render(request, "finalproject/memo.html", {
                "memos":memos,
                "form":NoteForm(),
                })
    else:
        return HttpResponseRedirect(reverse("login"))


# requesting the desired wake up time and needed sleep hours time.
#calculating with 12h format.
@csrf_exempt
def bed_time(request):
    form = BedtimeForm()
    if request.method == "POST":
        form = BedtimeForm(request.POST)
        if form.is_valid():
            wake = request.POST["Wake_up"]
            duration = request.POST["Duration"]
            ampm = request.POST["am_pm"]
            sleep_time = []

            # creating the 12 hour, 2 digit format to be shown on bed_time page.
            h = int(wake[:2]) - int(duration[:2])
            m = int(wake[-2:]) - int(duration[-2:])
            sleep_time.append('{:02}:{:02}'.format((h-1)%12 if m < 0 else h%12, m%60))
            if wake < duration:
                if ampm == "AM":
                    ampm = "PM"
                else:
                    ampm = "AM"
            else:
                ampm = ampm
            i = [x for x in sleep_time]
            return render(request, "finalproject/bed_time.html", {
                        "form":form,
                        "wake":wake,
                        "duration":duration, 
                        "ampm":ampm,
                        "i":i, 
                        "sleep_time":sleep_time
                    } )
        else:
            return render(request, "finalproject/bed_time.html", {
            "form":BedtimeForm(),
        })
    else:
        return render(request, "finalproject/bed_time.html", {
            "form":BedtimeForm(),
        })


# aquiring needed data before creating the chart on nutritions page
@csrf_exempt
def nutrition(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            nform = NutritionForm(request.POST)
            if nform.is_valid():
                counted=nform.cleaned_data["counted"]
                cosumed=nform.cleaned_data["cosumed"]
                category=nform.cleaned_data["category"]
                nutritions = Nutrition.objects.filter(category=category, n_user=request.user)

                # if logging one nutrition for the first time on this day, it will be saved in the table.
                if not nutritions:
                    nutri = Nutrition(n_date=timezone.datetime.now().strftime('%Y-%m-%d %H:%m:%S'), counted=counted, cosumed=cosumed, category=category, n_user=request.user)
                    nutri.save()
                else:

                    # if adding a nutrion to the previously created entry, only updates the amount in database.
                    nutri = Nutrition.objects.get(n_user=request.user, category=category)
                    c = nutri.counted
                    nutri.counted = counted + c
                    nutri.n_date = timezone.datetime.now().strftime('%Y-%m-%d %H:%m:%S')
                    nutri.save()

            # saving the entry in Sleep model
            sleeps = Sleep.objects.filter(s_user=request.user, todayis=datetime.now().strftime('%Y-%m-%d'), categorytoday=category)
            if not sleeps:
                s = Sleep(s_user=request.user, counttoday=nform.cleaned_data["counted"], categorytoday=nform.cleaned_data["category"], todayis=datetime.now().strftime('%Y-%m-%d'))
                s.save()
            else:

                # changes the data after first entry of the day for each category
                sums = Sleep.objects.get(s_user=request.user, categorytoday=category, todayis=datetime.now().strftime('%Y-%m-%d'))
                s = sums.counttoday
                sums.counttoday = counted + s
                sums.todayis = datetime.now().strftime('%Y-%m-%d')
                sums.save()
            return redirect("nutrition")
        
        else:
            nutritions = Nutrition.objects.all().order_by("category")
            return render(request, "finalproject/nutrition.html", {
                "nutritions":nutritions,
                "nform":NutritionForm(),
            })
    else:
        return HttpResponseRedirect(reverse("login"))
    

@csrf_exempt 

# showing the daily nutrition intake on chart vs max daily amounts
def sleepdaily(request):
    todays = Sleep.objects.filter(s_user=request.user).order_by("categorytoday")
    if not todays:
        return redirect("sleepdaily")
    else:
        return render(request, "finalproject/sleepdaily.html", {
                        "todays":Sleep.objects.filter(s_user=request.user, todayis=datetime.today().strftime('%Y-%m-%d')).order_by("categorytoday"),
                        "d":datetime.today(),
                        "nutritions":Nutrition.objects.all()
                    }) 


# setting the digital alarm
@csrf_exempt
def alarm(request):
    return render(request, "finalproject/alarm.html")


# add or edit the momos and save in the related table
@csrf_exempt 
def edit(request, note_id):
    if request.method == "POST":  
        try:
            memos = Note.objects.get(pk=note_id)
            note_id = memos.id
        except Note.DoesNotExist:
            return JsonResponse({"error": "Note not found."}, status=404)
        data = json.loads(request.body)
        if data.get("my_note") is not None:
            memos.my_note = data["my_note"]
            memos.note_date = timezone.now()
            memos.save()
        return JsonResponse({"my_note":memos.my_note}, status=200)
    elif request.method == "GET":
        return HttpResponseRedirect(reverse, "memo")
    else:
        return JsonResponse({"error":"error"})


def login_view(request):
    if request.method == "POST":
        reminder = request.POST["reminder"]
        password = request.POST["password"]
        user = authenticate(request, username=reminder, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "finalproject/login.html", {
                "message": "Invalid"
            })
    else:
        return render(request, "finalproject/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        reminder = request.POST["reminder"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "finalproject/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(reminder, reminder, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "finalproject/register.html", {
                "message": "reminder address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "finalproject/register.html")