"""sistemas_cuentas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to u'rlpatterns:  path('blog/', include('blog.urls'))
"""
#PUEDO HACER LAS PLANTILLAS CON  RETURNS DEL HTTPRESPONSE PERO QUIERO HACERLO CON RENDER
from django.contrib import admin
from django.urls import path, include
from sistemas_cuentas.views import index
from sistemas_cuentas.views import saludo #DESDE LA MISMA CARPETA

urlpatterns = [  
   path('', include('gestion_usuarios.urls')), #para acedder a otra ruta en otra carpeta
   path('index/', index), #de la misma carpeta
   path('saludo/', saludo), #de la misma carpeta
   path('', include('gestion_supervisor.urls')),#debe salir sin nada para continuar la ruta
   path('', include('gestion_presupuesto.urls')),
   path('', include('gestion_tesoreria.urls')),
   path('', include('gestion_identidades.urls')),
   path('', include('gestion_bitacora.urls')),
   path('', include('gestion_apis.urls')),
   
   
   #parte administrativa
   path('admin/', admin.site.urls, name='admin'),

   

  
]
