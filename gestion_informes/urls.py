from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import render, redirect
from django.conf.urls.static import static

urlpatterns = [
    #### estas urls son de ejemplo de como quiero el frontend de informes
    path('informe', views.informe, name='informe'), #vista django
  
] 