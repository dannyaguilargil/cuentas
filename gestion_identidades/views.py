from django.shortcuts import render
from django.contrib import messages
########################################
from django.http.response import JsonResponse
from django.http import JsonResponse
from gestion_usuarios.models import usolicitudes
from gestion_identidades.models import solicitudsistema

def identidades(request):
    return render(request, 'identidades.html')

def pazysalvo(request):
    return render(request, 'pazysalvo.html')

##aqui debe ir como traigo ese dato en json ""
def usolicitud(request):
    usuarios = list(solicitudsistema.objects.values())
    data = {'solicitud': usuarios}
    return JsonResponse(data)
## aqui debe ir como traigo los sistemas pendientes en json ###

def identidadespendientes(request):
    #solicitud_obj = ""
    datos = solicitudsistema.objects.values()
    return render(request, 'pendientes.html', {'datos': datos})
