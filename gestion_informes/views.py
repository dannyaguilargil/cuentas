from django.shortcuts import render, redirect
from gestion_informes.models import informe,entecontrol,dependencia,entrega,alarma,evidencia
from gestion_usuarios.models import usolicitudes
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from gestion_usuarios.models import usuario
from gestion_informes.forms import fente,fdependencia,ReviewForm,finforme,fevidencia
from django.contrib import messages
from django.views.generic.edit import FormView
#### configuracion de alarmas
from .tasks import enviar_alarma,enviar_alarma2
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
#####REUERIDOS PARA EL CALCULO DE ENTREGAS#####
from dateutil.relativedelta import relativedelta
from django.conf import settings


@login_required
def informes(request):
    #print("SESSION_EXPIRE_AT_BROWSER_CLOSE:", settings.SESSION_EXPIRE_AT_BROWSER_CLOSE)
    #print("SESSION_COOKIE_AGE:", settings.SESSION_COOKIE_AGE)
    username = request.user.username
    entes_control = entecontrol.objects.all()
    entes_dependencia = dependencia.objects.all()
    ### inserccion del informe ##
    finformes = finforme(request.POST, request.FILES)
    if finformes.is_valid():
        informe = finformes.save()
        messages.success(request, 'Informe agregado correctamente.')
        nombre_informe = informe.nombre

        ####configuracion de envios de tareas programadas#####
        print("Informe creado exitosamente")
        nombre_responsable = request.POST.get('nombreresponsable')
        correo_responsable = request.POST.get('correoresponsable')##no lo paso por formulario, debo mirar como lo tomo
        print(nombre_responsable)
        print(correo_responsable)
        dias_anticipacion = int(request.POST.get('alarmas'))
        ########cargando las otras dos alarmas######
        dias_anticipacion2 = int(request.POST.get('alarmas2') or 0)
        dias_anticipacion3 = int(request.POST.get('alarmas3') or 0)
        #############################################
        print(dias_anticipacion)
        print(dias_anticipacion2)
        print(dias_anticipacion3)
        fecha_entrega_inicial = datetime.strptime(request.POST.get('fechaentregainicial'), '%Y-%m-%d')
        print(fecha_entrega_inicial)
        fecha_alarma = fecha_entrega_inicial - timedelta(days=dias_anticipacion)
        ########cargando las otras dos alarmas######
        fecha_alarma2 = fecha_entrega_inicial - timedelta(days=dias_anticipacion2)
        fecha_alarma3 = fecha_entrega_inicial - timedelta(days=dias_anticipacion3)
        ########cargando las otras dos alarmas######
        print(fecha_alarma)
        mensaje_html = f"""
            <html>
            <body>
                <p>{nombre_responsable},</p>
                <p>Está a <b style="color: green;">{dias_anticipacion} días</b> de la fecha LIMITE para entregar el informe: <strong>{informe.nombre}</strong> al ente de control: <strong>{informe.entecontrol}</strong>.</p>
                <p>Fecha límite: <strong>{informe.fechaentregainicial}</strong></p>
                <p>Recuerde que debe <strong>ENVIAR</strong> el ticket en la mesa de ayuda para que la oficina de <b style="color: green">INFORMATICA</b> pueda validar la información <b>A TIEMPO</b>.</p>
                <p><a type="button" href="http://sara.imsalud.gov.co:8000/informe/entrega/{informe.id}">Ver informe</a> | <a type="button" href="https://soporte.imsalud.gov.co">Mesa de ayuda</a></p>
            </body>
            </html>
            """
            
            # Envío del correo de alarma
        enviar_alarma2.apply_async(
            args=[correo_responsable, mensaje_html, nombre_informe],
            eta=fecha_alarma
        )
        ########cargando las otras dos alarmas###### 
        enviar_alarma2.apply_async(
            args=[correo_responsable, mensaje_html, nombre_informe],
            eta=fecha_alarma2
        )
        
        enviar_alarma2.apply_async(
            args=[correo_responsable, mensaje_html, nombre_informe],
            eta=fecha_alarma3
        )
        ########cargando las otras dos alarmas######     

        ###AQUI VA LA CREACION AUTOMATICAS DE LAS ENTREGAS### 
        periodicidad = int(request.POST.get('periodicidad'))
        periodicidadtipo = request.POST.get('periodicidadtipo')
        totalentregas = int(request.POST.get('totalentregas'))
        fecha_entrega = fecha_entrega_inicial

        for i in range(totalentregas):
            entrega.objects.create(informe=informe, fecha=fecha_entrega, activo=True)
            print(f"Entrega {i + 1}: Fecha de entrega {fecha_entrega}")
            if periodicidadtipo == 'Dias':
                fecha_entrega += timedelta(days=periodicidad)
            elif periodicidadtipo == 'Meses':
                fecha_entrega += relativedelta(months=periodicidad)
            else:
                print(f"Tipo de periodicidad no reconocido: {periodicidadtipo}")
                break  
        return redirect('informe')
        ###AQUI VA LA CREACION AUTOMATICAS DE LAS ENTREGAS### 


    else:
        finformes = finforme()
        print("Rednderizado")
    pertenece_a_informes = request.user.groups.filter(name='informes').exists()
    es_staff = request.user.is_staff
    return render(request, 'informes.html', {'entes_control': entes_control, 'entes_dependencia': entes_dependencia, 'finformes': finformes, 'username': username, 'pertenece_a_informes': pertenece_a_informes,
                                             'es_staff': es_staff}) 

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
     username = request.user.username
     es_staff = request.user.is_staff
     datos = informe.objects.all().select_related('entecontrol', 'dependencia')#para busqueda relacionada en cascada
     return render(request, 'listado.html', {'datos': datos, 'username': username, 'es_staff': es_staff}) 

#@login_required
#def  entecontrols(request):
#     datos = entecontrol.objects.values()
#     formper = fente(request.POST or None)
#     if formper.is_valid():
#        formper.save()
#        messages.success(request, 'Ente de control agregado.')
#        return redirect('entecontrol')
     ######Formulario de actualizacion del ente de control
#     return render(request, 'entecontrol.html', {'datos': datos, 'formper': formper}) 
@login_required
def entecontrols(request):
    username = request.user.username
    if request.method == 'POST':
        # Comprobamos si es una actualización o una creación
        if 'nombre_act' in request.POST:  
            # Actualización
            ente_id = request.POST.get('ente_id')
            ente = get_object_or_404(entecontrol, id=ente_id)
            ente.nombre = request.POST.get('nombre_act')
            ente.descripcion = request.POST.get('descripcion_act')
            if ente.nombre:  # Validación mínima
                ente.save()
                messages.success(request, 'Ente de control actualizado.')
            else:
                messages.error(request, 'Error al actualizar el ente de control.')
        else:
            # Creación
            form = fente(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ente de control agregado.')
            else:
                messages.error(request, 'Error al agregar el ente de control.')
        return redirect('entecontrol')
    
    # GET request
    datos = entecontrol.objects.values()
    formper = fente()
    es_staff = request.user.is_staff
    return render(request, 'entecontrol.html', {'datos': datos, 'formper': formper, 'username': username, 'es_staff': es_staff})

@login_required
def dependencias(request):
    username = request.user.username
    if request.method == 'POST':
        # Comprobamos si es una actualización o una creación
        if 'nombre_act' in request.POST:
            # Actualización
            dep_id = request.POST.get('dep_id')
            dep = get_object_or_404(dependencia, id=dep_id)
            dep.nombre = request.POST.get('nombre_act')
            dep.responsable = request.POST.get('responsable_act')
            dep.correoresponsable = request.POST.get('correoresponsable_act')
            if dep.nombre:  # Validación mínima
                dep.save()
                messages.success(request, 'Dependencia actualizada.')
            else:
                messages.error(request, 'Error al actualizar la dependencia.')
        else:
            # Creación
            form = fdependencia(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Dependencia agregada.')
            else:
                messages.error(request, 'Error al agregar la dependencia.')
        return redirect('dependencias')
    
    # GET request
    datos = dependencia.objects.values()
    formpers = fdependencia()
    es_staff = request.user.is_staff
    return render(request, 'dependencia.html', {'datos': datos, 'formpers': formpers, 'username': username, 'es_staff': es_staff})
## en entregas debe trarse el id del informe
@login_required
def  entregar(request, id):
     username = request.user.username
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
     alarmas3 = informes.alarmas3 # pendiente configurar alarmas segn cantidades para la notificacion y el frontend
     forevidencia = ''

     if request.method == 'POST':
        forevidencia = fevidencia(request.POST, request.FILES)
        if forevidencia.is_valid():
            forevidencia.save()
            messages.success(request, 'Evidencia entregada')
            return redirect('entrega', id=id)
        else :
            messages.error(request, 'No se realizo el cargue de evidencias')
            print("NO se realizo el cargue de evidencias")
     es_staff = request.user.is_staff
     return render(request, 'entrega.html', {'nombre': nombre, 'normativa': normativa, 'entecontrol': entecontrol, 'dependencia': dependencia,
     'fechaentregainicial': fechaentregainicial, 'periodicidad': periodicidad, 'periodicidadtipo': periodicidadtipo, 'totalentregas': totalentregas,
     'activo': activo, 'descripcion': descripcion, 'dias': dias, 'fechaentregapendiente': fechaentregapendiente, 'responsable': responsable,
     'correoresponsable': correoresponsable, 'entregas': entregas, 'entregas_con_evidencias': entregas_con_evidencias, 'alarmas': alarmas,
     'alarmas2': alarmas2, 'alarmas3': alarmas3, 'forevidencia': forevidencia, 'username': username, 'es_staff': es_staff } ) 

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
    username = request.user.username
    ### por ahora comentados, pero la idea es que si pueda cambiar el ente de control y dependencia##
    controles = entecontrol.objects.all()
    depende = dependencia.objects.all()
    
    informes = get_object_or_404(informe, id=id)
    nombre = informes.nombre
    normativa = informes.normativa
    entecontrols = informes.entecontrol
    dependencias = informes.dependencia
    fechaentregainicial = informes.fechaentregainicial
    fechaentregapendiente = informes.fechaentregapendiente
    periodicidad = informes.periodicidad
    periodicidadtipo = informes.periodicidadtipo
    totalentregas = informes.totalentregas
    activo = informes.activo
    descripcion = informes.descripcion
    ####campos para ser actualizados###
    es_staff = request.user.is_staff

    ### inserccion del informe ##
    return render(request, 'informes-actualizar.html', {'nombre': nombre, 'entecontrols': entecontrols, 'dependencias': dependencias, 'descripcion': descripcion,
    'fechaentregainicial': fechaentregainicial, 'username': username, 'es_staff': es_staff, 'periodicidad': periodicidad, 'periodicidadtipo': periodicidadtipo,
    'totalentregas': totalentregas}) 

#opcion de eliminar aqui
@login_required
def informeeliminar(request, id):
    inform = informe.objects.get(id=id)
    inform.delete()
    return redirect('listado')
#opcion de eliminar aqui   