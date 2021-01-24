from django.shortcuts import render
from django.http import HttpResponse
from .models import VendorPost


# Create your views here.
def index(request):
    return render(request, 'home.html', {})

def create_business(request):
    return render(request, 'create_business.html', {})

def account_info(request):
    return render(request, 'account_info.html', {})

def vendor_info(request):
    
    return render(request, 'vendor_info.html', {})

def business_info(request):
    vendors = VendorPost.objects.all()

    context = {'vendor':vendors}
    return render(request, 'business_info.html', context)

