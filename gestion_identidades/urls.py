from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render

urlpatterns = [

    path('identidades', views.identidades, name='identidades'),
    path('identidades/pazysalvo', views.pazysalvo, name='pazysalvo'),
    path('identidades/pendientes', views.identidadespendientes, name='identidadespendientes'),
    path('identidades/list_pendientes', views.usolicitud, name='identidades_list_pendientes'),
    path('identidades/pendientes/admin', views.identidadespendientesadmin, name='identidadespendientesadmin'),
   
]