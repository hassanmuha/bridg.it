from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('companies/',views.companies, name='companies'), 
    path('delete/',views.delete, name='delete'),
    path('update/',views.update, name='update')   
]