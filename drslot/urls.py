"""
URL configuration for drslot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appointments import views as appointments_views

HANDLER404 = 'appointments.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Use appointments_views.index
    path('', appointments_views.index, name='index'),
    path(
        'appointments/',
        appointments_views.my_appointments,
        name='appointments'
    ),
    path('register/', appointments_views.register, name='register'),
    path('booking/', appointments_views.booking, name='booking'),
    path(
        'my_appointments/',
        appointments_views.my_appointments,
        name='my_appointments'
    ),
    path('accounts/', include('allauth.urls')),
    path('delete_appointment/<int:appointment_id>/',
         appointments_views.delete_appointment,
         name='delete_appointment'),
    path('edit_appointment/<int:appointment_id>/',
         appointments_views.edit_appointment, name='edit_appointment'),
]
