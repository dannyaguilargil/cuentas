
from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('base', views.base, name='base'),
    path('prueba', views.prueba, name='prueba'),
    path('login', views.home, name='inicio'),
    path('login', views.logout, name='logout'),
    path('usuarios', views.usuarios, name='usuarios'), 
    path('usuarios/solicitud', views.solicitud_usuario, name='solicitud_usuario'), 
    path('usuarios/crear', views.crear, name='crear'), 
    path('usuarios/documentos', views.documentos, name='documentos'), 
    path('perfil', views.perfil, name='perfil'), 
    path('usuarios/sdocumentos', views.documentos_usuario, name='documentos_usuario'), 
    path('list_usuarios', views.list_usuarios, name='list_usuarios'), 
    path('usuarios/pendientes', views.usuarios_pendientes, name='usuarios_pendientes'),
    path('list_pendientes', views.usolicitud, name='list_pendientes'),
    ##########ELIMINAR EL REGISTRO ###################################### 
    path('usuarios/pendient/eliminar/<int:cedula>', views.eliminar, name='eliminar'), 
    path('usuarios/pendient/guardar/<int:cedula>', views.guardar, name='guardar'),
    #path('usuarios/documentos/registro', views.registro, name='registro'), 
    ##########GESTION DE USUARIOS PENDIENTES ### CRUD DIFERENTE
    path('usuarios/pendiente/', views.usuario_pendiente, name='usuario_pendiente'),
    path('usuarios/pendiente/<int:cedula>', views.obtenercedula, name='obtenercedula'),
    path('eliminarregistro/', views.eliminarregistro, name='eliminarregistro'),
    path('usuarios/pendient/', views.usuarios_pendient, name='usuario_pendient'),
    path('eliminador/<int:cedula>/', views.eliminador, name='eliminador'),
       #path('admin/', admin.site.urls,name='admin'),
    #path('usuarios/pendient/guardar/<int:cedula>', views.eliminar, name='eliminar'), 
    
    
    #################### nuevos cambios
    path('contratista/perfil', views.ops, name='ops'),
    path('contratista/cuentas', views.cuentas, name='cuentas'),
 
  
]