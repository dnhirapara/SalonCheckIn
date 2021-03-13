from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SalonRegistrationForm, RegistrationForm
from django.contrib.auth import authenticate, login
from utils.send_email import send_email
from .models import Account
# Create your views here.


def register(request):
    context = {}
    context['title'] = 'Register'
    if request.method == 'POST':
        salon_form = SalonRegistrationForm(request.POST)
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid() and salon_form.is_valid():
            user = user_form.save()
            salon = salon_form.save(commit=False)
            salon.user = user
            salon_form.save()
            email = user_form.cleaned_data.get('email').lower()
            raw_password = user_form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            redirect('accounts/index.html', context)
            # return render(request, 'accounts/index.html', context)
        else:
            context['user_form'] = user_form
            context['salon_form'] = salon_form
    else:
        user_form = RegistrationForm()
        salon_form = SalonRegistrationForm()
        context['user_form'] = user_form
        context['salon_form'] = salon_form
    return render(request, 'accounts/shop_register.html', context)


def loginSalon(request):
    context = {}
    context['title'] = 'Login'
    return render(request, 'accounts/shop_login.html', context)


def index(request):
    context = {}
    send_email()
    context['title'] = 'index'
    return render(request, 'accounts/index.html', context)
