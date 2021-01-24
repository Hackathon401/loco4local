from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'home.html', {})

def create_business(request):
    return render(request, 'create_business.html', {})

def vendor_info(request):
    return render(request, 'vendor_info.html', {})

def business_info(request):
    return render(request, 'business_info.html', {})

