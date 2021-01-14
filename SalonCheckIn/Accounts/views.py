from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):
    context = {}
    context['title'] = 'Register'
    return render(request, 'accounts/shop_register.html', context)


def login(request):
    context = {}
    context['title'] = 'Login'
    return render(request, 'accounts/shop_login.html', context)
