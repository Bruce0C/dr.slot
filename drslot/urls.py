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
from django.contrib.auth.views import LoginView
from django.urls import path, include
from appointments.views import my_appointments, index
from home import views as home_views

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('appointments/', my_appointments, name='appointments'),
# path('', include('home.urls')),
# Ensure the 'index' view is defined in home/views.py
#    path('', views.index, name='index'),
#    path('register/', views.register, name='register'),
#    path('login/', 'django.contrib.auth.views.LoginView.as_view()', name='login'),
#    path('booking/', views.booking, name='booking'),
#    path('my_appointments/', views.my_appointments, name='my_appointments'),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index, name='index'),  # Corrected index view
    path('appointments/', my_appointments, name='appointments'),
    path('register/', home_views.register, name='register'),  # Corrected
    path('login/', LoginView.as_view(), name='login'),
    path('booking/', home_views.booking, name='booking'),  # Corrected
    path('my_appointments/', home_views.my_appointments,
         name='my_appointments'),  # Corrected
]
