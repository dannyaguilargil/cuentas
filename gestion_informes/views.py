from django.shortcuts import render, redirect
from gestion_informes.models import informe
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
    usuarios = list(usolicitudes.objects.values())
    data = {'informe': usuarios}
    return JsonResponse(data)
###listado de informe ###

#ejemplo con solicitudes de usuarios provisionalmente
def  listado(request):
     usuarios = list(usolicitudes.objects.values())
     datos = {'informe': usuarios}
     return render(request, 'listado.html', {'datos': datos}) 

def  entecontrol(request):
     return render(request, 'entecontrol.html') 

def  dependencias(request):
     return render(request, 'dependencia.html') 
