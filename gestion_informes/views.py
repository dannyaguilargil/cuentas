from django.shortcuts import render, redirect
from gestion_informes.models import informe,entecontrol,dependencia,entrega,alarma,evidencia
from gestion_usuarios.models import usolicitudes
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from gestion_usuarios.models import usuario
from gestion_informes.forms import fente,fdependencia,ReviewForm,finforme
from django.contrib import messages
from django.views.generic.edit import FormView
#### configuracion de alarmas
from .tasks import enviar_alarma
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def informes(request):
    entes_control = entecontrol.objects.all()
    entes_dependencia = dependencia.objects.all()
    ### inserccion del informe ##
    finformes = finforme(request.POST, request.FILES)
    if finformes.is_valid():
        finformes.save()
        messages.success(request, 'Informe agregado correctamente.')

        ####configuracion de envios de tareas programadas#####
        correo_responsable = request.POST.get('correoresponsable')
        dias_anticipacion = int(request.POST.get('alarmas'))
        fecha_entrega_inicial = datetime.strptime(request.POST.get('fechaentregainicial'), '%Y-%m-%d')
        fecha_alarma = fecha_entrega_inicial - timedelta(days=dias_anticipacion)

        ###enviar la tarea de alarma
        enviar_alarma.apply_async(
            args=[correo_responsable, f'Alarma para el informe: {informe.nombre}'],
            eta=fecha_alarma
        )
        ###enviar la tarea de alarma

        ####configuracion de envios de tareas programadas#####

        return redirect('informe')
    finformes = finforme()
    ### inserccion del informe, revisar que se haga inserccion con alarma ##

    return render(request, 'informes.html', {'entes_control': entes_control, 'entes_dependencia': entes_dependencia, 'finformes': finformes }) 

#ejemplo con solicitudes de usuarios provisionalmente
@login_required
def listado_informe(request):
    usuarios = list(informe.objects.values())
    data = {'informe': usuarios}
    return JsonResponse(data)

###listado de informe ###
@login_required
def listadoente(request):
    entes = list(entecontrol.objects.values())
    data = {'entes': entes}
    return JsonResponse(data)

@login_required
def listadodependencia(request):
    entes = list(dependencia.objects.values())
    data = {'dependencias': entes}
    return JsonResponse(data)
###listado de informe ###

#ejemplo con solicitudes de usuarios provisionalmente
@login_required
def  listado(request):
     datos = informe.objects.all().select_related('entecontrol', 'dependencia')#para busqueda relacionada en cascada
     return render(request, 'listado.html', {'datos': datos}) 

@login_required
def  entecontrols(request):
     datos = entecontrol.objects.values()
     formper = fente(request.POST or None)
     if formper.is_valid():
        formper.save()
        messages.success(request, 'Ente de control agregado.')
        return redirect('entecontrol')
     return render(request, 'entecontrol.html', {'datos': datos, 'formper': formper}) 

@login_required
def  dependencias(request):
     datos = dependencia.objects.values()
     formpers = fdependencia(request.POST or None)
     if formpers.is_valid():
        formpers.save()
        messages.success(request, 'Dependencia agregado.')
        return redirect('dependencias')
     return render(request, 'dependencia.html', {'datos': datos, 'formpers': formpers}) 

## en entregas debe trarse el id del informe
@login_required
def  entregar(request, id):
     informes = get_object_or_404(informe, id=id)

     dependencia = informes.dependencia
     responsable = ""
     correoresponsable = ""

     if dependencia:
         responsable = dependencia.responsable
         correoresponsable = dependencia.correoresponsable

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

     ####ONTIENE TODA LAS ENTREGAS DEL INFORME############
     entregas = entrega.objects.filter(informe=informes)
     #### EVIDENCIAS ASOCIADAS A CADA ENTREGA #############
     entregas_con_evidencias = []
     for entrega_obj in entregas:
         evidencias = evidencia.objects.filter(entrega=entrega_obj)   
         entregas_con_evidencias.append({
            'entrega': entrega_obj,
            'evidencias': evidencias
         })


     normativa = informes.normativa
     entecontrol = informes.entecontrol
     fechaentregainicial = informes.fechaentregainicial
     fechaentregapendiente = informes.fechaentregapendiente
     periodicidad = informes.periodicidad
     periodicidadtipo = informes.periodicidadtipo
     totalentregas = informes.totalentregas
     activo = informes.activo
     descripcion = informes.descripcion
     alarmas = informes.alarmas
     alarmas2 = informes.alarmas2
     alarmas3 = informes.alarmas3
     ###modificar para etregar alarmas segun la cantidad#####


     return render(request, 'entrega.html', {'nombre': nombre, 'normativa': normativa, 'entecontrol': entecontrol, 'dependencia': dependencia,
     'fechaentregainicial': fechaentregainicial, 'periodicidad': periodicidad, 'periodicidadtipo': periodicidadtipo, 'totalentregas': totalentregas,
     'activo': activo, 'descripcion': descripcion, 'dias': dias, 'fechaentregapendiente': fechaentregapendiente, 'responsable': responsable,
     'correoresponsable': correoresponsable, 'entregas': entregas, 'entregas_con_evidencias': entregas_con_evidencias, 'alarmas': alarmas,
     'alarmas2': alarmas2, 'alarmas3': alarmas3 } ) 

@login_required
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

@login_required
def  prueba(request):
     return render(request, 'tareasprueba.html') 

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponse(msg)

@login_required
def informeactualizar(request, id):
    ### por ahora comentados, pero la idea es que si pueda cambiar el ente de control y dependencia##
    #controles = entecontrol.objects.all()
    #depende = dependencia.objects.all()
    ###toca asociarlo#####################

    ####campos para ser actualizados###
    informes = get_object_or_404(informe, id=id)
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
    ####campos para ser actualizados###


    ### inserccion del informe ##
    return render(request, 'informes-actualizar.html', {'nombre': nombre, 'entecontrol': entecontrol, 'dependencia': dependencia, 'descripcion': descripcion,
    'fechaentregainicial': fechaentregainicial}) 

#opcion de eliminar aqui
@login_required
def informeeliminar(request, id):
    inform = informe.objects.get(id=id)
    inform.delete()
    return redirect('listado')
#opcion de eliminar aqui   