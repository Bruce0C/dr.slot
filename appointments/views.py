from django.shortcuts import render, redirect
from .models import Service

# Create your views here.


def index(request):
    return render(request, 'appointments/index.html')


def register(request):
    return render(request, 'appointments/register.html')


def booking(request):
    services = Service.objects.all()
    validateWeekdays = ['2026-10-25',
                        '2026-10-26', '2026-10-27']  # Example data
    return render(request, 'appointments/booking.html', {
        'services': services,
        'validateWeekdays': validateWeekdays
    })


def my_appointments(request):
    return render(request, 'appointments/my_appointments.html')


def user_login(request):
    return render(request, 'appointments/login.html')


def user_logout(request):
    return redirect('login')  # Redirect to login page after logout
