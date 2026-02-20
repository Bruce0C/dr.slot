"""
This module registers the models from the appointments app
to the Django admin interface, allowing administrators to
manage appointments, services, availability, reviews, and notifications.

Admins can perform CRUD operations on these models through the admin panel.
"""
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.contrib import admin
from .models import Appointment, Service, Availability
admin.site.register(Appointment)
# Register your models here.

admin.site.register(Service)
admin.site.register(Availability)


class Command(BaseCommand):
    help = 'Create default user groups and permissions'

    def handle(self, *args, **kwargs):
        # Create Patient group
        patient_group, created = Group.objects.get_or_create(name='Patient')
        if created:
            self.stdout.write('Patient group created')

        # Create Doctor group
        doctor_group, created = Group.objects.get_or_create(name='Doctor')
        if created:
            self.stdout.write('Doctor group created')

        self.stdout.write('Default groups created successfully')
