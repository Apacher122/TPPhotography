from django.shortcuts import render
from django.http import HttpResponse

# Create views

def home(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html",{})

def contact(request, *args, **kwargs):
    return render(request, "contact.html",{})

def about(request, *args, **kwargs):
    return render(request, "about.html",{})

def portfolio(request, *args, **kwargs):
    return render(request, "portfolio.html",{})