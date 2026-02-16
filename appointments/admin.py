"""
This module registers the models from the appointments app
to the Django admin interface, allowing administrators to
manage appointments, services, availability, reviews, and notifications.

Admins can perform CRUD operations on these models through the admin panel.
"""
from django.contrib import admin
from .models import Appointment, Service, Availability
admin.site.register(Appointment)
# Register your models here.

admin.site.register(Service)
admin.site.register(Availability)
