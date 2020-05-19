from django.shortcuts import render, redirect
from django.http import HttpResponse
from pymongo import MongoClient
from django.views.generic import TemplateView
from .forms import HomeForm
# Create your views here.


class ProductView(TemplateView):
    template_name='Product/index.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['post']      
        return redirect("products")       

        arg={'form':form, 'text':text}
        return render(request, self.template_name, arg)

def prodSave(request):
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.products

    new_Product={
            'pname' : "Brick",
            'productCode' : "789",
            'manufacturedYear' : "2020",
            'manufacturedMonth' : "02",
            'pdescription' : "It is a brick updated description",
            'price' : "10",
            'location' : "melbourne"
        }
    records.insert_one(new_Product)

    return HttpResponse("Product Saved")


def findByName(request):

    cNameQuery={ "name": "bridgit Pr." }
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.products
    firstData= records.find_one()


    return HttpResponse("HTML Tem will add here...... for Company/products")




def products(request):
    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.products
    firstData= records.find_one()

    arrProd=[]
    for x in records.find():
        arrProd.append(x)

    
    return HttpResponse("HTML Tem will add here...... for Company/products")

def delete(request):
    myquery = { "name": "Brick" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.products
    conArr = records.delete_one(myquery)

    return HttpResponse("Deleted")


def update(request):
    myquery = { "name": "Brick" }

    client=MongoClient('mongodb+srv://morisha:bridgit@bridgit-euhfa.mongodb.net/test?retryWrites=true&w=majority')
    db=client.get_database('bridgit')
    records=db.products


    newvalues = { "$set": {  'name' : "Brick",
                             'productCode' : "789",
                             'manufacturedYear' : "2020",
                             'manufacturedMonth' : "02",
                             'description' : "It is a brick updated description"

                 } }
    records.update_one(myquery, newvalues)

    return HttpResponse("Updated")
