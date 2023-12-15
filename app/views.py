from django.shortcuts import render

# Create your views here.
from app.models import *


def display_Country(request):
    QLTO=Country.objects.all()
    d={'Country':QLTO}
    return render(request,'display_Country.html',d)