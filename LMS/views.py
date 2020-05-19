from django.shortcuts import render, redirect
from django.http import HttpResponse
from pymongo import MongoClient
from django.views.generic import TemplateView
from Company.forms import HomeForm

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


def userRegister(request):
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.user
    new_user={
        'username':"hassan@deakin.com",
        'name':"Muhammad Hassan",
        'email':"hassan@gmail.com",
        'dob':'1990-01-01T13:00:00.000+00:00',
        'password':"12345",
        'active':'true',
    }
        
    records.insert_one(new_user)
    return HttpResponse("User Registered")

def delete(request):
    myquery = { "name": "Hassan" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.user
    conArr = records.delete_one(myquery)

    return HttpResponse("User Deleted")


def update(request):
    myquery = { "name": "Muhammad Hassan" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.user
    newvalues = { "$set": { 'username':"Muhammad Hassan",
                            'name':"Hassan",
                            'email':"hassan@gmail.com",
                            'dob':'1990-01-01T13:00:00.000+00:00',
                            'password':"12345",
                            'active':'true',
                 } }
    records.update_one(myquery, newvalues)
    return HttpResponse("User Updated")



