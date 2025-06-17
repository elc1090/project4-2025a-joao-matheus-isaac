from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def custom_logout(request):
    logout(request)
    return redirect(
        'https://accounts.google.com/Logout?continue='
        'https://appengine.google.com/_ah/logout?continue='
        'http://localhost:8000/'
    )
