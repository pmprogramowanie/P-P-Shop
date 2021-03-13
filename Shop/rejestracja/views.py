from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rejestracja.forms import RegisterForm


# Create your views here.
def rejestracja(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/kategoria")
    else:
        form = RegisterForm()

    return render(response, "rejestracja.html", {"form": form})

