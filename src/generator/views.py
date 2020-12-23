from django.urls import reverse
from django.shortcuts import render, redirect
from .utils import generate_password


def index(request):
    context = {"message": "get password"}
    return render(request, 'generator/index.html', context)


def get_password(request):
    password = generate_password(request)
    context = {"message": "get another password", "password": password}
    return render(request, 'generator/index.html', context)
