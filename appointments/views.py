from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, Appointment
from datetime import datetime, timedelta


# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def my_appointments(request):
    """
    A view to display the user's appointments.
    """
    appointments = Appointment.objects.filter(user=request.user)
    return render(
        request,
        'appointments/my_appointments.html',
        {'appointments': appointments}
    )


def validWeekday(days):
    """
    Generate a list of valid weekdays for the next 'days' days.
    """
    today = datetime.now().date()
    weekdays = [(today + timedelta(days=i)).strftime('%Y-%m-%d')
                for i in range(days)]
    return weekdays


def isWeekdayValid(weekdays):
    """
    Filter weekdays to exclude fully booked days.
    For simplicity, this example assumes no days are fully booked.
    """
    # Add logic to filter out fully booked days if needed
    return weekdays


@login_required
def booking(request):
    """
    A view to handle appointment booking.
    """
    # Fetch available services
    services = Service.objects.all()

    # Get available weekdays (next 21 days)
    weekdays = validWeekday(22)

    # Only show the days that are not fully booked
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service_id = request.POST.get('service')
        day = request.POST.get('day')

        # Validate service selection
        if not service_id:
            messages.error(request, "Please select a service!")
            return redirect('booking')

        # Validate day selection
        if not day or day not in validateWeekdays:
            messages.error(request, "Please select a valid day!")
            return redirect('booking')

        # Create the appointment
        service = Service.objects.get(id=service_id)
        Appointment.objects.create(
            user=request.user,
            service=service,
            day=day,
            time_created=datetime.now()
        )
        messages.success(
            request, "Your appointment has been successfully booked!")
        return redirect('my_appointments')

    return render(request, 'appointments/booking.html', {
        'services': services,
        'validateWeekdays': validateWeekdays
    })
