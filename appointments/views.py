"""
Views for the appointment booking system. This module contains all the views
"""
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Service, Appointment, TIME_CHOICES, SERVICE_CHOICES
from django.contrib.auth.decorators import user_passes_test


def is_patient(user):
    """Check if the user is in the Patient group."""
    return user.groups.filter(name='Patient').exists()


def is_doctor(user):
    """Check if the user is in the Doctor group."""
    return user.groups.filter(name='Doctor').exists()


def index(request):
    """View to render the homepage of the appointment booking system."""
    is_patient = request.user.groups.filter(
        name='Patient').exists() if request.user.is_authenticated else False
    is_doctor = request.user.groups.filter(
        name='Doctor').exists() if request.user.is_authenticated else False
    return render(request, 'appointments/index.html', {
        'is_patient': is_patient,
        'is_doctor': is_doctor,
    })


def register(request):
    """View to handle user registration."""
    form = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            # Assign the user to the Patient group by default
            patient_group = Group.objects.get(name='Patient')
            user.groups.add(patient_group)
            messages.success(
                request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(
                request,
                "There was an error with your registration. Please try again."
            )

    return render(request, 'appointments/register.html', {'form': form})


def service_view(request):
    """
    View to display available services.
    This view is accessible to all users.
    """
    return render(request, 'appointments/service.html', {
        'service_choices': Service.objects.all()
    })


@login_required
@user_passes_test(is_patient)
def booking(request):
    """View to handle appointment booking for patients."""
    services = Service.objects.all()

    if request.method == 'POST':
        service_id = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Validate form inputs
        if not service_id or not date or not time:
            messages.error(request, "Please fill out all fields.")
            return render(
                request,
                'appointments/booking.html',
                {'services': services}
            )

        # Validate date format
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            messages.error(
                request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(
                request,
                'appointments/booking.html',
                {'services': services}
            )

        # Save the appointment
        try:
            service = Service.objects.get(id=service_id)
            Appointment.objects.create(
                user=request.user,
                service=service,
                date=date,
                time=time
            )
            # Add success message
            messages.success(request, "Booking created successfully!")
            return redirect('my_appointments')
        except Service.DoesNotExist:
            messages.error(request, "The selected service does not exist.")
            return render(
                request,
                'appointments/booking.html',
                {'services': services}
            )

    return render(request, 'appointments/booking.html', {'services': services})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Doctor').exists())
def all_appointments(request):
    """View to display all appointments (for doctors)."""
    appointments = Appointment.objects.all().order_by('-date', '-time')
    return render(request, 'appointments/all_appointments.html', {
        'appointments': appointments
    })


@login_required
def my_appointments(request):
    """View to display the user's appointments."""
    appointments = Appointment.objects.filter(
        user=request.user).order_by('-date', '-time')
    user_is_patient = request.user.groups.filter(name='Patient').exists()
    user_is_doctor = request.user.groups.filter(name='Doctor').exists()
    return render(request, 'appointments/my_appointments.html', {
        'appointments': appointments,
        'is_patient': user_is_patient,
        'is_doctor': user_is_doctor,
    })


@login_required
def edit_appointment(request, appointment_id):
    """View to edit an existing appointment."""
    appointment = get_object_or_404(
        Appointment, id=appointment_id, user=request.user)
    services = Service.objects.all()

    if request.method == 'POST':
        service_id = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Validate form inputs
        if not service_id or not date or not time:
            messages.error(request, "Please fill out all fields.")
            return render(request, 'appointments/edit_appointment.html', {
                'appointment': appointment,
                'services': services,
            })

        # Validate date format
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            messages.error(
                request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(request, 'appointments/edit_appointment.html', {
                'appointment': appointment,
                'services': services,
            })

        # Update the appointment
        try:
            service = Service.objects.get(id=service_id)
            appointment.service = service
            appointment.date = date
            appointment.time = time
            appointment.save()
            messages.success(request, "Appointment updated successfully!")
            return redirect('my_appointments')
        except Service.DoesNotExist:
            messages.error(request, "The selected service does not exist.")
            return render(request, 'appointments/edit_appointment.html', {
                'appointment': appointment,
                'services': services,
            })

    return render(request, 'appointments/edit_appointment.html', {
        'appointment': appointment,
        'services': services,
    })


@login_required
def delete_appointment(request, appointment_id):
    """View to delete an appointment."""
    appointment = get_object_or_404(
        Appointment, id=appointment_id, user=request.user)

    if request.method == "POST":
        appointment.delete()
        messages.success(request, "Appointment deleted successfully!")
        return redirect('my_appointments')

    return render(request, 'appointments/confirm_delete.html', {'appointment': appointment})


def user_login(request):
    """View to handle user login"""
    return render(request, 'appointments/login.html')


def user_logout(request):
    """View to handle user logout."""
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to login page after logout


def error_404_view(request, _exception):
    """Custom 404 error handler."""
    return render(request, 'appointments/error_404.html', status=404)
