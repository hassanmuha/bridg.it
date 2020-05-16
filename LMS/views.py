from django.shortcuts import render, redirect
from django.http import HttpResponse
from pymongo import MongoClient

# Create your views here.

def login(request):
    return render(request,'LMS/login/index.html')

def loginPost(request):
    myquery = { "email": request.GET['userEmail'] }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.user
    copData = records.find_one(myquery)
    
    if copData is None:
        return redirect('/company/companies/')
    else:
        return redirect('/lms/login')


def home(request):
    return render(request,'LMS/landingPage/index.html')
