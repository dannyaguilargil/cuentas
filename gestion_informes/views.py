from django.shortcuts import render, redirect
from gestion_informes.models import informe,entecontrol,dependencia
from gestion_usuarios.models import usolicitudes
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from gestion_usuarios.models import usuario

# Create your views here.
def  informes(request):
     return render(request, 'informes.html') 

#ejemplo con solicitudes de usuarios provisionalmente
def listado_informe(request):
    usuarios = list(informe.objects.values())
    data = {'informe': usuarios}
    return JsonResponse(data)
###listado de informe ###

def listadoente(request):
    entes = list(entecontrol.objects.values())
    data = {'entes': entes}
    return JsonResponse(data)
###listado de informe ###

def listadodependencia(request):
    entes = list(dependencia.objects.values())
    data = {'dependencias': entes}
    return JsonResponse(data)
###listado de informe ###

#ejemplo con solicitudes de usuarios provisionalmente
def  listado(request):
     datos = informe.objects.values()
     return render(request, 'listado.html', {'datos': datos}) 

def  entecontrols(request):
     datos = entecontrol.objects.values()
     return render(request, 'entecontrol.html', {'datos': datos}) 

def  dependencias(request):
     datos = dependencia.objects.values()
     return render(request, 'dependencia.html', {'datos': datos}) 
