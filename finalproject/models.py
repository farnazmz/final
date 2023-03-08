from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass


class Nutrition(models.Model):
    CATEGORIES= [
    ('Protein', 'Protein: Max 50g'),
    ('Fat', 'Fat: Max 65g'),
    ('SaturatedFattyAcids', 'Saturated Fatty Acids: Max 20g'),
    ('Carbohydrates', 'Carbohydrates: Max 304g'),
    ('Sugars', 'Sugars: Max 38g'),
    ('Sodium', 'Sodium: Max 2.3g'),
    ('DietaryFibre', 'DietaryFibre: Max 25g'),
    ] 

    n_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="n_user")
    n_date = models.DateTimeField(timezone.now, blank="True", null="True")
    cosumed = models.TextField(max_length=64, null="True")
    counted = models.IntegerField(null="True") 
    category = models.CharField(max_length=50, choices=CATEGORIES, default="Protein")

    


class Note(models.Model):
    this_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="this_user")
    note_date = models.DateTimeField(timezone.now, blank="True", null="True")
    my_note = models.TextField(max_length=1000)
    

class Sleep(models.Model):
    s_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="s_user")
    todayis = models.DateTimeField(timezone.now, blank="True", null="True")
    wake = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    duration = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    sleep_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True) 
    counttoday = models.IntegerField(blank=True, null=True) 
    categorytoday = models.CharField(max_length=50, blank=True, null=True)

    

        