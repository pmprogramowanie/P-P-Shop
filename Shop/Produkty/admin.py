from django.contrib import admin
from .models import Produkty, Producent, Kategoria, Koszyk

# Register your models here.

admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Koszyk)
