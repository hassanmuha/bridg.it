from django.conf.urls import url
from django.urls import path    
from Product.views import ProductView
from . import views

urlpatterns = [
    url(r'^$',ProductView.as_view(), name='index'),
    path('products/',views.products, name='products'),   
    path('delete/',views.delete, name='delete'),
    path('update/',views.update, name='update'), 
    path('prodSave/',views.prodSave,name='prodSave'), 
     ]

