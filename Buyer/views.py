from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("HTML Tem will add here...... for buyer")
    return render(request,'buyer/index.html')

def products(request):
    return HttpResponse("HTML Tem will add here...... for buyer/products")