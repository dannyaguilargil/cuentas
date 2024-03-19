
from django.contrib import admin
from django.urls import path, include
#from .views import home
from . import views
from django.shortcuts import render
from rest_framework import routers
#from bitacora import views

router = routers.DefaultRouter()
router.register(r'bitacora', views.bitacoraView, 'bitacora')

urlpatterns = [
    path('', include(router.urls))

]