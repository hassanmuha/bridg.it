from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("HTML Tem will add here...... for Product")
    return render(request, 'Product/index.html')

def products(request):
    return HttpResponse("HTML Tem will add here...... for Product/products")