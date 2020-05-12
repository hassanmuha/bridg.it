from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('buyer/',views.products, name='products'),
]
