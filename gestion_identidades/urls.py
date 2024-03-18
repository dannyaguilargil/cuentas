from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render

urlpatterns = [

    path('identidades', views.identidades, name='identidades'),
   
]