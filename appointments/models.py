from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

SERVICE_CHOICES = (
    ("Doctor care", "Nurse care"),
    ("Nursing care", "Nursing care"),
)
TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)


class Service(models.Model):
    """
    Model to represent the services offered by the platform.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """
    Model to represent appointments booked by patients.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_created = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ("Pending", "Pending"),
            ("Confirmed", "Confirmed"),
            ("Cancelled", "Cancelled"),
            ("Completed", "Completed"),
        ),
        default="Pending",
    )

    def __str__(self):
        username = self.user.username if self.user else 'No user'
        return f"{username} | {self.service.name} | {self.day} at {self.time}"


class Availability(models.Model):
    """
    Model to represent a doctor's availability.
    """
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return (
            f"{self.doctor.username} | {self.day} | "
            f"{self.start_time} - {self.end_time}"
        )
