
from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
   
    path('nuevaeps/afiliacion', views.nuevaeps, name='nuevaeps'), #Datos de afiliacion
    path('nuevaeps/basicos', views.nuevaepsbasicos, name='nuevaepsbasicos'), #Datos basicos de afiliacion
    path('nuevaeps/contacto', views.nuevaepscontacto, name='nuevaepscontacto'), #Datos de contacto
   
]