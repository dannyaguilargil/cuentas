from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import render, redirect
from django.conf.urls.static import static

urlpatterns = [
    #### estas urls son de ejemplo de como quiero el frontend de informes
    path('informe/listado_informe', views.listado_informe, name='listado_informe'),
    path('informe', views.informes, name='informe'), #vista django pasarla a vuejs
    path('informe/listado', views.listado, name='listado'), #solo django
    path('informe/ente-control', views.entecontrols, name='entecontrol'), #solo django
    path('informe/listado_ente', views.listadoente, name='listadoente'), #JSON ente de control
    path('informe/dependencias', views.dependencias, name='dependencias'), #solo django
    path('informe/listado_dependencia', views.listadodependencia, name='listadodependencia'), #JSON dependencia
    path('informe/entrega/<int:id>', views.entrega, name='entrega'), #solo django
    path('informe/nombre_responsable', views.obtener_nombre_responsable, name='nombre_responsable'),
] 