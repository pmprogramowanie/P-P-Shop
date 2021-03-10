# urls.py
from django.urls import path
from rejestracja import views

urlpatterns = [

path("rejestracja/", views.rejestracja, name="rejestracja"),

]