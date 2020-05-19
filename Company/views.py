from django.shortcuts import render, redirect
from django.http import HttpResponse
from pymongo import MongoClient
from django.views.generic import TemplateView
from Company.forms import HomeForm

# Create your views here.


class CompanyView(TemplateView):
    template_name='Company/index.html'
    

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['post']
            

        # client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
        # db=client.get_database('bridgit')
        # records=db.companies
        # new_Company={
        # 'name' : "Tom",
        # 'twitter_usrname' : "Tim",
        # 'category_code' : "1213",
        # 'number of employees' : "95",
        # 'founded year' : "2020",
        # 'founded month' : "01",
        # 'email address': "info@tomtim.com",
        # 'phone' : "000000000",
        # 'desription' : "TomTim co.",
        # 'overview' : "It is a division of XYZ company. It deals with making of Color sche...",
        # 'relationships': "Brother",
        # 'products':"Brick"
        # }
        # records.insert_one(new_Company)
            
        return redirect("companies")
        

        arg={'form':form, 'text':text}
        return render(request, self.template_name, arg)



def compSave(request):
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies

    new_Company={
            'name' : "ABC Co.",
            'twitter_usrname' : "ABC co.",
            'category_code' : "1213",
            'number of employees' : "95",
            'founded year' : "2020",
            'founded month' : "01",
            'email address': "info@ABC.com",
            'phone' : "000000000",
            'desription' : "TomTim co.",
            'overview' : "It is a division of XYZ company. It deals with making of Color sche...",
            'relationships': "Brother",
            'products':"Brick",
        }
    records.insert_one(new_Company)

    return HttpResponse("Company Saved")


# def index(request):
#     client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
#     db=client.get_database('bridgit')
#     records=db.companies
#     conArr = records.count_documents({})
#     absd="this is test"
#     return render(request, 'Company/index.html', {'absd':absd})


def findByName(request):

    cNameQuery={ "name": "bridgit Co." }
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies
    firstData= records.find_one()


    return HttpResponse("HTML Tem will add here...... for Company/products")




def companies(request):
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies
    firstData= records.find_one()

    arrComp=[]
    for x in records.find():
        arrComp.append(x)

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
    myquery = { "name": "Hassan" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies
    conArr = records.delete_one(myquery)

    return HttpResponse("Deleted")


def update(request):
    myquery = { "name": "Muhammad" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.companies


    newvalues = { "$set": {  'name' : "Muhammad Hassan",
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
    records.update_one(myquery, newvalues)

    return HttpResponse("Updated")