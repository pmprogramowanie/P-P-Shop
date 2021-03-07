from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Produkty, Kategoria
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(response):
    if response.method == "POST":
        dane = RegisterForm(response.POST)
        if dane.is_valid():
            dane.save
        return redirect("http://127.0.0.1:8000/")
    else:
        dane = RegisterForm()
    return render(response, "register.html", {"dane": dane})


def index(request):
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=1)
    kat = Produkty.objects.filter(kategoria=1)
    producent = Produkty.objects.get(id=1)
    kat_name = Kategoria.objects.get(id=3)
    null = Produkty.objects.filter(kategoria__isnull=False)
    zawiera = Produkty.objects.filter(opis__icontains='karty')
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_produkt': kategoria_produkt,
            'kategorie': kategorie}
    return render(request, 'kategoria_produkt.html', dane)


def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)
