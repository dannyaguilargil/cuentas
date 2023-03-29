
from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='inicio'),
    path('usuarios', views.usuarios, name='usuarios'), 
    path('usuarios/solicitud', views.solicitud_usuario, name='solicitud_usuario'), 
    path('usuarios/crear', views.crear, name='crear'), 
    path('usuarios/documentos', views.documentos, name='documentos'), 
    path('perfil', views.perfil, name='perfil'), 
    path('usuarios/sdocumentos', views.documentos_usuario, name='documentos_usuario'), 
]