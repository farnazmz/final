from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bed_time", views.bed_time, name="bed_time"),
    path("memo", views.memo, name="memo"),
    path("alarm", views.alarm, name="alarm"),
    path("nutrition", views.nutrition, name="nutrition"),
    path("sleepdaily", views.sleepdaily, name="sleepdaily"),
    path("edit", views.edit, name="edit"),
    path("edit/memos/<int:note_id>", views.edit, name="edit"),
]