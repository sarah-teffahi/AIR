from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
import os
from django.contrib.auth import logout

# Create your views here.


#def admin(request):
       # return render(request, 'admin/base.html')

def home(request):
    return render(request, 'admin\home.html')