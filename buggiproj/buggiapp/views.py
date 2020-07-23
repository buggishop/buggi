from django.shortcuts import render
from buggiapp.models import User
from buggiapp.models import Shop
from buggiapp.models import Address_shop
from buggiapp.models import Address_user

# Create your views here.

def home_page(request):
    return render(request,'buggi_home.html')