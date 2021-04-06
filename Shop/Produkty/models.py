from django.db import models


class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Producent'
        verbose_name_plural = 'Producenci'


class Kategoria(models.Model):
    objects = True

    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


class Produkty(models.Model):
    objects = True
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=9999, decimal_places=2)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'


class Koszyk(models.Model):
    objects = None
    Produkty = models.ForeignKey(Produkty, null=True, blank=True, on_delete=models.CASCADE)
    produkt = models.CharField(max_length=30)
    ilosc = models.DecimalField(max_digits=9999, decimal_places=2)
    cena = models.DecimalField(max_digits=9999, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.nazwa = None

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = 'Koszyk'
        verbose_name_plural = 'Koszyk'
