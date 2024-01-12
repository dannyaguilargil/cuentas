
from django.contrib import admin
from django.urls import path, include
#from .views import home
from . import views
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from .views import extraer_texto


urlpatterns = [
    #path('admin/', admin.site.urls),
   
    #path('admin-redireccion/', lambda request: redirect('admin/')),
    path('base', views.base, name='base'),
    path('prueba', views.prueba, name='prueba'),
    path('login', views.home, name='inicio'),
    path('login', views.logout, name='logout'),
    path('usuarios', views.usuarios, name='usuarios'), 
    path('usuarios/solicitud', views.solicitud_usuario, name='solicitud_usuario'), 
    path('usuarios/crear', views.crear, name='crear'), 
    path('usuarios/documentos', views.documentos, name='documentos'),## GESTION DE GESCON
    path('perfil', views.perfil, name='perfil'), 
    path('usuarios/sdocumentos', views.documentos_usuario, name='documentos_usuario'), 
    path('list_usuarios', views.list_usuarios, name='list_usuarios'), 
    path('usuarios/pendientes', views.usuarios_pendientes, name='usuarios_pendientes'),
    path('list_pendientes', views.usolicitud, name='list_pendientes'),
    ##########ELIMINAR EL REGISTRO ###################################### 
    path('usuarios/pendient/eliminar/<int:cedula>', views.eliminar, name='eliminar'), ###ESTE ES EL QUEHACE LA ELIMINACION
    path('usuarios/pendient/guardar/<int:cedula>', views.guardar, name='guardar'),
    #path('usuarios/documentos/registro', views.registro, name='registro'), 
    ##########GESTION DE USUARIOS PENDIENTES ### CRUD DIFERENTE
    path('usuarios/pendiente/', views.usuario_pendiente, name='usuario_pendiente'),
    path('usuarios/pendiente/<int:cedula>', views.obtenercedula, name='obtenercedula'),
    path('eliminarregistro/', views.eliminarregistro, name='eliminarregistro'),
    path('usuarios/pendient/', views.usuarios_pendient, name='usuario_pendient'),
    path('eliminador/<int:cedula>/', views.eliminador, name='eliminador'),
    #path('eliminador/<int:cedula>/', views.eliminador, name='eliminador'),
       #path('admin/', admin.site.urls,name='admin'),
    #path('usuarios/pendient/guardar/<int:cedula>', views.eliminar, name='eliminar'), 
    #################### nuevos cambios
    path('contratista/perfil', views.ops, name='ops'),#############################PAGINA PRINCIPAL ##########
    path('contratista/cuentas', views.cuentas, name='cuentas'),
    path('contratista/actapago/<int:cedula>/', views.pruebapdf, name='actapago'),
    path('contratista/actapagohtml', views.pruebapdfactapago, name='pruebapdfactapago'),
    path('contratista/seguimientohtml', views.seguimientohtml, name='seguimientohtml'),
    path('contratista/seguimiento/<int:cedula>/', views.seguimiento, name='seguimiento'),
    path('extraer/', views.extraer_texto, name='extraer_texto'),
    #path('contratista/perfil/<int:cedula>/', views.actualizar_usuario, name='actualizar_usuario'),
  
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)