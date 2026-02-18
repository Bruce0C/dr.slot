from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, 'appointments/index.html')


def register(request):
    return render(request, 'appointments/register.html')


def booking(request):
    return render(request, 'appointments/booking.html')


def my_appointments(request):
    return render(request, 'appointments/my_appointments.html')
