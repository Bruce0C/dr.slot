from datetime import date
from django.db import models
from django.contrib.auth.models import User


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
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """
    Model to represent an appointment between a user and a service.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)  # Default user ID
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.service.name} on {self.date} "
            f"at {self.time}"
        )


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
