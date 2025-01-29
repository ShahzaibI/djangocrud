from django.shortcuts import render
from django.http import HttpResponse
from home.models import Car
import random
# Create your views here.

def home(request):
    Car.objects.create(car_name=f"Nexon-{random.randint(0, 100)}", speed=100)
    peoples = [
        {'name' : 'Muhammad Sarfraz', 'age' : 25},
        {'name' : 'Shahzaib Islam', 'age' : 22},
        {'name' : 'Haider Saeed', 'age' : 22},
        {'name' : 'Zaeem khan', 'age' : 22},
        {'name' : 'Danial Qamar', 'age' : 16},
    ]
    return render(request, 'index.html', context={'page' : 'Home' ,'peoples' : peoples})

def about(request):
    context = {'page' : 'About'}
    return render(request, 'about.html', context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, 'contact.html', context)