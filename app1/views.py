from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'app1/dashboard.html')

def products(request):
    return render(request,'app1/products.html')

def customers(request):
    return render(request,'app1/customer.html')
