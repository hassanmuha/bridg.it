from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('loginPost/', views.loginPost, name='loginPost'),
    path('userRegister/',views.userRegister, name='userRegister'),
    path('delete/',views.delete, name='delete'),
    path('update/',views.update, name='update'),
]
