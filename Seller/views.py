from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("HTML Tem will add here...... for Seller")
    #return render(request, '')

def sellers(request):
    return HttpResponse("HTML Tem will add here...... for seller/sellers")