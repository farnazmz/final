from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Nutrition, Note

# Register your models here.
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Nutrition)