from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, Appointment

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})


@login_required
def booking(request):
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

        # Check if the service exists
        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            messages.error(request, "Invalid service selected!")
            return redirect('booking')

        # Store day and service in Django session
        request.session['day'] = day
        request.session['service'] = service_id

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'services': services,
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
    })
