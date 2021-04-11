from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(req):
    form = UserCreationForm()
    return render(req, 'register.html', {'form': form})