from django.shortcuts import render

# Create your views here.
# filepath: /path/to/home/views.py
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Home Page!")
