"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from Produkty.views import kategoria, produkt, index
from rejestracja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("rejestracja/", views.rejestracja, name="rejestracja"),
    path("", include("rejestracja.urls")),
    path('', include("django.contrib.auth.urls")),
    path('', index, name=' index'),
    path('kategoria/<id>/', kategoria, name='kategoria'),
    path('produkt/<id>/', produkt, name='produkt'),

]