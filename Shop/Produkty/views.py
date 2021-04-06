from django.shortcuts import render
from .models import Produkty, Kategoria, Koszyk


def index(request):
    # wszystkie = Produkty.objects.all()
    # jeden = Produkty.objects.get(pk=1)
    # kat = Produkty.objects.filter(kategoria=1)
    # producent = Produkty.objects.get(id=1)
    # kat_name = Kategoria.objects.get(id=3)
    # null = Produkty.objects.filter(kategoria__isnull=False)
    # zawiera = Produkty.objects.filter(opis__icontains='karty')
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


def koszyk(request, id):
    koszyk_user = Koszyk.objects.get(pk=id)
    dane = {'koszyk_user': koszyk_user, 'koszyk': koszyk}
    return render(request, 'koszyk.html', dane)
