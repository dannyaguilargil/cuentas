from django.shortcuts import render, redirect
from gestion_informes.models import informe,entecontrol,dependencia
from gestion_usuarios.models import usolicitudes
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from gestion_usuarios.models import usuario
from gestion_informes.forms import fente,fdependencia
from django.contrib import messages


def  informes(request):
     entes_control = entecontrol.objects.all()
     entes_dependencia = dependencia.objects.all()
     return render(request, 'informes.html', {'entes_control': entes_control}) 

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


def listadodependencia(request):
    entes = list(dependencia.objects.values())
    data = {'dependencias': entes}
    return JsonResponse(data)
###listado de informe ###

#ejemplo con solicitudes de usuarios provisionalmente
def  listado(request):
     datos = informe.objects.all().select_related('entecontrol', 'dependencia')#para busqueda relacionada en cascada
     return render(request, 'listado.html', {'datos': datos}) 

def  entecontrols(request):
     datos = entecontrol.objects.values()
     formper = fente(request.POST or None)
     if formper.is_valid():
        formper.save()
        messages.success(request, 'Ente de control agregado.')
        return redirect('entecontrol')
     return render(request, 'entecontrol.html', {'datos': datos, 'formper': formper}) 

def  dependencias(request):
     datos = dependencia.objects.values()
     formpers = fdependencia(request.POST or None)
     if formpers.is_valid():
        formpers.save()
        messages.success(request, 'Dependencia agregado.')
        return redirect('dependencias')
     return render(request, 'dependencia.html', {'datos': datos, 'formpers': formpers}) 

def  entrega(request):
     return render(request, 'entrega.html') 
