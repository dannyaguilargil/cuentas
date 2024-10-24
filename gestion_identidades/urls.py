from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render

urlpatterns = [

    path('identidades', views.identidades, name='identidades'),
    path('identidades/pazysalvo', views.pazysalvos, name='pazysalvo'),
    path('identidades/pendientes', views.identidadespendientes, name='identidadespendientes'),
    # para elminar solicitud path('identidades/pendientes', views.identidadespendientes, name='identidadespendientes'),

    path('identidades/list_pendientes', views.usolicitud, name='identidades_list_pendientes'),
    path('identidades/pendientes/list_admin', views.listadmin, name='listadmin'),
    path('identidades/pendientes/admin', views.identidadespendientesadmin, name='identidadespendientesadmin'),
    ############ejemplo para la generacion del pdf ####################
    #path('contratista/seguimiento/<int:cedula>/', views.seguimiento, name='seguimiento'),
    path('identidades/certificado', views.pazysalvohtml, name='pazysalvohtml'),
    path('identidades/certificado/<int:cedula>', views.certificado, name='certificado'),
    path('identidades/listadoaplicativos', views.listadoaplicativos, name='listadoaplicativos'), #JSON aplicativos
    path('identidades/modulos', views.listadomodulos, name='listadomodulos'), #JSON aplicativos
    path('identidades/listadopazysalvo', views.solicitudespaz, name='solicitudespaz'),
    path('identidades/pazysalvo/listado', views.pazysalvolistado, name='pazysalvolistado'),
    path('identidades/perfil', views.identidadesperfil, name='identidadesperfil'),
    path('identidades/acuerdoc', views.acuerdoc, name='acuerdoc'),
    path('identidades/tratamiento', views.tratamiento, name='tratamiento'),
    path('identidades/tratamiento/<int:cedula>', views.tratamientodp, name='tratamientodp'),
]