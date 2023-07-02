
from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render


urlpatterns = [
    #path('admin/', admin.site.urls),
    #ath('', views.saludo2),p
#   path('', views.saludo2),
#    path('saludo/', views.saludo3),
    path('supervisor', views.supervisor, name='supervisor'),
    path('supervisor/actapago/<int:cedula>', views.pruebapdf, name='actapagosupervisor'),
    path('supervisor/actapagohtml', views.pruebapdfactapago, name='pruebapdfactapago'),
    path('supervisor/seguimientohtml', views.seguimientohtml, name='seguimientohtml'),
    path('supervisor/seguimiento/<int:cedula>/', views.seguimiento, name='seguimientosupervisor'),
    path('supervisor/eliminar/<int:cedula>', views.eliminar, name='eliminarsupervisor'),
    #path('supervisorflujo/<int:cedula>', views.supervisorflujo, name='supervisorflujo'),
]