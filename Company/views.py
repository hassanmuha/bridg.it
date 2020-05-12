from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from models import mdl
# Create your views here.

    


def index(request):
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies
    conArr = records.count_documents({})
    absd="this is test"
    return render(request, 'Company/index.html', {'absd':absd})


def companies(request):
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies
    firstData= records.find_one()

    arrComp=[]
    for x in records.find():
        arrComp.append(x)

    nameCom= mdl.company.name
    # new_Company={
    #     'name' : "Alex",
    #     'twitter_usrname' : "Pettter",
    #     'category_code' : "1213",
    #     'number of employees' : "95",
    #     'founded year' : "2020",
    #     'founded month' : "01",
    #     'email address': "info@alex.com",
    #     'phone' : "000000000",
    #     'desription' : "Alec co.",
    #     'overview' : "It is a division of XYZ company. It deals with making of Color sche...",
    #     'relationships': "Brother",
    #     'products':"Brick"
    # }

   # records.insert_one(new_Company)
    return HttpResponse("HTML Tem will add here...... for Company/products")

def delete(request):
    myquery = { "name": "Alex" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies
    conArr = records.delete_one(myquery)

    return HttpResponse("Deleted")


def update(request):
    myquery = { "name": "Alex" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies

    copData = records.find_one(myquery)

    newvalues = { "$set": {  'name' : "Muhammad",
                             'twitter_usrname' : "Hassan",
                             'category_code' : "1213",
                             'number of employees' : "95",
                             'founded year' : "2020",
                             'founded month' : "01",
                             'email address': "info@alex.com",
                             'phone' : "000000000",
                             'desription' : "Hassan co.",
                             'overview' : "It is a division of XYZ company. It deals with making of Color sche...",
                             'relationships': "Brother",
                             'products':"Brick"
                 } }
    records.update_one(copData, newvalues)

    return HttpResponse("Updated")