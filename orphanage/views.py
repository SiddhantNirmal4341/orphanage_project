from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm

def home(request): return render(request, 'home.html')
def about(request): return render(request, 'about.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user: login(request, user); return redirect('home')
        else: messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('success')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def adoption_view(request):
    form = AdoptionForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('success')
    return render(request, 'adoption_form.html', {'form': form})

def donation_view(request):
    form = DonationForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('success')
    return render(request, 'donation_form.html', {'form': form})

def volunteer_view(request):
    form = VolunteerForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('success')
    return render(request, 'volunteer_form.html', {'form': form})

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('success')
    return render(request, 'contact.html', {'form': form})

def success_view(request): return render(request, 'success.html')
