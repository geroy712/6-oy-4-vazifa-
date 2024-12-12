from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Car

def index(request: WSGIRequest):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, "intex.html", context)

def bmw(request: WSGIRequest):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, 'bmw.html', context)