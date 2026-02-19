from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Service, Appointment, TIME_CHOICES, TIME_CHOICES


def index(request):
    """View to render the homepage of the appointment booking system."""
    return render(request, 'appointments/index.html')


def register(request):
    """View to handle user registration. """
    return render(request, 'appointments/register.html')


def service_view(request):
    """
    View to display available services.
    This view is accessible to all users.
    """
    return render(request, 'appointments/service.html', {
        'service_choices': Service.objects.all()
    })


@login_required
def booking(request):
    """View to handle appointment booking."""
    services = Service.objects.all()

    if request.method == 'POST':
        service_id = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Validate form inputs
        if not service_id or not date or not time:
            messages.error(request, "Please fill out all fields.")
            return render(request, 'appointments/booking.html', {
                'services': services,
            })

        # Save the appointment
        try:
            service = Service.objects.get(id=service_id)
            Appointment.objects.create(
                user=request.user,
                service=service,
                date=date,
                time=time
            )
            messages.success(
                request, "Your appointment has been booked successfully!")
            # Redirect to "My Appointments" page
            return redirect('my_appointments')
        except Service.DoesNotExist:
            messages.error(request, "The selected service does not exist.")
            return render(request, 'appointments/booking.html', {
                'services': services,
            })

    return render(request, 'appointments/booking.html', {
        'services': services,
    })


@login_required
def my_appointments(request):
    """View to display the user's appointments."""
    appointments = Appointment.objects.filter(
        user=request.user).order_by('-date', '-time')
    return render(request, 'appointments/my_appointments.html', {
        'appointments': appointments
    })


def user_login(request):
    """View to handle user login"""
    return render(request, 'appointments/login.html')


def user_logout(request):
    """View to handle user logout."""
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to login page after logout
