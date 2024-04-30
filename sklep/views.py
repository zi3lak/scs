from django.shortcuts import render
from .models import Produkt
from django.http import HttpResponse

def lista_produktow(request):
    produkty = Produkt.objects.all()
    return render(request, 'sklep/lista_produktow.html', {'produkty': produkty})

def home(request):
    return HttpResponse("Witaj na stronie głównej!")
