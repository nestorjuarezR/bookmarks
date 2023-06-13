from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

#Index
def index(request):
    return render(request, "./account/index.html")


