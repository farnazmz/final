from django import forms

class NutritionForm(forms.Form):
    cosumed = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"cosumed", "PlaceHolder":"consumed"}))
    counted = forms.IntegerField(label="", widget=forms.NumberInput(attrs={"class":"counted", "PlaceHolder":"Counted"}))
    category = forms.CharField(label="", widget=forms.Select(choices=[
    ('Protein', 'Protein: Max 50g'),
    ('Fat', 'Fat: Max 65g'),
    ('SaturatedFattyAcids', 'SaturatedFattyAcids: Max 20g'),
    ('Carbohydrates', 'Carbohydrates: Max 304g'),
    ('Sugars', 'Sugars: Max 38g'),
    ('Sodium', 'Sodium: Max 2.3g'), 
    ('DietaryFibre', 'DietaryFibre: Max 25g')
 ], attrs={"class":"category"}))


class NoteForm(forms.Form):
    my_note = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"note", "PlaceHolder":"memo..."}))
CATEGORIES= [
    ('AM', 'AM'),
    ('PM', 'PM'),
 ]


class BedtimeForm(forms.Form):
    Wake_up = forms.TimeField(label="", widget=forms.TextInput(attrs={"class":"bed", "PlaceHolder":"Wake Up"}))
    Duration = forms.TimeField(label="", widget=forms.TextInput(attrs={"class":"bed", "PlaceHolder":"Duration"}))
    am_pm = forms.CharField(label="", widget=forms.Select(choices=CATEGORIES))