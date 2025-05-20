# orphanage/forms.py
from django import forms
from .models import Adoption, Donation, Volunteer, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
