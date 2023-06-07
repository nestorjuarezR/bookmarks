from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

#Index
def index(request):
    return render(request, "./account/index.html")

#Login de usuarios
