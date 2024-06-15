from django.contrib import admin
from django.urls import path, include
#from .views import home
from . import views
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('siau/cexterna', views.consultaexterna, name='consultaexterna'),
    path('siau/odontologia', views.odontologia, name='odontologia'),
    path('siau/enfermeria', views.enfermeria, name='enfermeria'),
]