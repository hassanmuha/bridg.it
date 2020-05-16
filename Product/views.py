from django.shortcuts import render, redirect
from django.http import HttpResponse
from pymongo import MongoClient
from django.views.generic import TemplateView
from Product.forms import HomeForm
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
    return render(request, 'Product/saved.html')

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

    copData = records.find_one(myquery)

    newvalues = { "$set": {  'name' : "Brick",
                             'productCode' : "789",
                             'manufacturedYear' : "2020",
                             'manufacturedMonth' : "02",
                             'description' : "It is a brick updated description"
                 } }
    records.update_one(copData, newvalues)

    return HttpResponse("This is the products Updated page")

