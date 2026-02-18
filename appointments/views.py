from django.shortcuts import render, redirect
from .models import Service, Appointment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'appointments/index.html')


def register(request):
    return render(request, 'appointments/register.html')


@login_required
def booking(request):
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

    return render(request, 'appointments/booking.html', {
        'services': services,
    })

    # Save the appointment
    service = Service.objects.get(id=service_id)
    Appointment.objects.create(
        user=request.user,
        service=service,
        date=date,
        time=time
    )
    messages.success(
        request, "Your appointment has been booked successfully!")
    return redirect('my_appointments')

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
