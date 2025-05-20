# orphanage/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reset-password/', password_reset_view, name='reset_password'),
    path('adopt/', adoption_view, name='adopt'),
    path('donate/', donation_view, name='donate'),
    path('volunteer/', volunteer_view, name='volunteer'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
