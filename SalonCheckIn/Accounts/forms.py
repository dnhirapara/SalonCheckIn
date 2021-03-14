from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import Salon, Customer, Account


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')


class SalonRegistrationForm(ModelForm):
    class Meta:
        model = Salon
        fields = ('display_name', 'description')

# 'email', 'username', 'password1', 'password2',
