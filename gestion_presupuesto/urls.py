
from django.contrib import admin
from django.urls import path
#from .views import home
from . import views
from django.shortcuts import render

urlpatterns = [

    path('presupuesto', views.presupuesto, name='presupuesto'),
    #path('presupuesto/actapago/<int:cedula>', views.pruebapdf, name='actapagosupervisor'),
    #path('presupuesto/actapagohtml', views.pruebapdfactapago, name='pruebapdfactapago'),
    #path('presupuesto/seguimientohtml', views.seguimientohtml, name='seguimientohtml'),
    #path('presupuesto/seguimiento/<int:cedula>/', views.seguimiento, name='seguimientosupervisor'),
   
]