from django.shortcuts import render, redirect
from gestion_informes.models import informe,entecontrol,dependencia,entrega,alarma
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
     return render(request, 'informes.html', {'entes_control': entes_control, 'entes_dependencia': entes_dependencia }) 

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

## en entregas debe trarse el id del informe
def  entrega(request, id):
     informes = get_object_or_404(informe, id=id)
     ######revisar resultado de alarmas en revision
     try: 
         alarmas = alarma.objects.get(id=id)## para trearme toda las alarmas
         informe_id = alarmas.informe.id
         dias = alarmas.dias

     except alarma.DoesNotExist:
         dias = "No se encontraron alarmas"
      ######revisar resultado de alarmas en revision
     #dias = "En desarollo"

     nombre = informes.nombre
     normativa = informes.normativa
     entecontrol = informes.entecontrol
     dependencia = informes.dependencia
     fechaentregainicial = informes.fechaentregainicial
     fechaentregapendiente = informes.fechaentregapendiente
     periodicidad = informes.periodicidad
     periodicidadtipo = informes.periodicidadtipo
     totalentregas = informes.totalentregas
     activo = informes.activo
     descripcion = informes.descripcion
     return render(request, 'entrega.html', {'nombre': nombre, 'normativa': normativa, 'entecontrol': entecontrol, 'dependencia': dependencia,
     'fechaentregainicial': fechaentregainicial, 'periodicidad': periodicidad, 'periodicidadtipo': periodicidadtipo, 'totalentregas': totalentregas,
     'activo': activo, 'descripcion': descripcion, 'dias': dias, 'fechaentregapendiente': fechaentregapendiente } ) 


def obtener_nombre_responsable(request):
    dependencia_id = request.GET.get('dependencia_id')
    if dependencia_id:
        try:
            dependencia = dependencia.objects.get(pk=dependencia_id)
            return JsonResponse({'nombre': dependencia.responsable})
        except dependencia.DoesNotExist:
            return JsonResponse({'error': 'La dependencia no existe'}, status=404)
    else:
        return JsonResponse({'error': 'El parámetro dependencia_id es requerido'}, status=400)


def  prueba(request):
     return render(request, 'tareasprueba.html') 