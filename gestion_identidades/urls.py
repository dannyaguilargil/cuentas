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
    path('identidades/pendientes/list_admin', views.listadmin, name='listadmin'),
    path('identidades/pendientes/admin', views.identidadespendientesadmin, name='identidadespendientesadmin'),
    ############ejemplo para la generacion del pdf ####################
    #path('contratista/seguimiento/<int:cedula>/', views.seguimiento, name='seguimiento'),
    path('identidades/certificado', views.pazysalvohtml, name='pazysalvohtml'),
    path('identidades/certificado/<int:cedula>', views.certificado, name='certificado'),


]