from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, Availability, Appointment

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


@login_required
def booking(request):
    '''...'''
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to book an appointment.")
        return redirect('login')

    # Fetch available services
    services = Service.objects.all()

    # Get available weekdays (next 21 days)
    weekdays = validWeekday(22)

    # Only show the days that are not fully booked
    validateWeekdays = isWeekdayValid(weekdays)
