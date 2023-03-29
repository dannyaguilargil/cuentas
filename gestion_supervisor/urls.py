
from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render

urlpatterns = [
    #path('admin/', admin.site.urls),
    #ath('', views.saludo2),p
#   path('', views.saludo2),
#    path('saludo/', views.saludo3),
    path('supervisor', views.supervisor, name='supervisor'),
   
]