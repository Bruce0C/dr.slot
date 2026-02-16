from django.contrib import admin
from django.urls import path
from . import views
from appointments.views import my_appointments

urlpatterns = [
    path('', views.index, name='home'),
]
