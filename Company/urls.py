from django.conf.urls import url
from django.urls import path
from Company.views import CompanyView
from . import views

urlpatterns = [
    url(r'^$',CompanyView.as_view(), name='index'),
    # path('', views.index,name='index'),
    path('companies/',views.companies, name='companies'), 
    path('delete/',views.delete, name='delete'),
    path('update/',views.update, name='update'),
    path('compSave/',views.compSave,name='compSave'),  
]
