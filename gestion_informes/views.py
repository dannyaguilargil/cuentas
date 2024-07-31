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
from django.utils import timezone
#####################################
from operator import itemgetter

@login_required
def informes(request):
    username = request.user.username
    entes_control = entecontrol.objects.all()
    entes_dependencia = dependencia.objects.all()
    finformes = finforme(request.POST, request.FILES)
    if finformes.is_valid():
        informe = finformes.save()
        messages.success(request, 'Informe agregado correctamente.')
        nombre_informe = informe.nombre

        nombre_responsable = request.POST.get('nombreresponsable')
        correo_responsable = request.POST.get('correoresponsable')
        dias_anticipacion = int(request.POST.get('alarmas'))
        dias_anticipacion2 = int(request.POST.get('alarmas2') or 0)
        dias_anticipacion3 = int(request.POST.get('alarmas3') or 0)
        periodicidad = int(request.POST.get('periodicidad'))
        periodicidadtipo = request.POST.get('periodicidadtipo')
        totalentregas = int(request.POST.get('totalentregas'))
        fecha_entrega = datetime.strptime(request.POST.get('fechaentregainicial'), '%Y-%m-%d')
        
        for i in range(totalentregas):
            nueva_entrega = entrega.objects.create(informe=informe, fecha=fecha_entrega, activo=True)
            print(f"Entrega {i + 1}: Fecha de entrega {fecha_entrega}")
            
            # Calcular las fechas de las alarmas para esta entrega
            fecha_alarma = fecha_entrega - timedelta(days=dias_anticipacion)
            fecha_alarma2 = fecha_entrega - timedelta(days=dias_anticipacion2)
            fecha_alarma3 = fecha_entrega - timedelta(days=dias_anticipacion3)
            
            # Enviar las alarmas
            if dias_anticipacion > 0:
                mensaje_html = f"""
                    <html>
                    <body>
                        <p><span>{nombre_responsable}</span>,</p>
                        <p>Está a <span style="color: green">{dias_anticipacion} días</span> de la fecha LIMITE para entregar el informe: <strong>{informe.nombre}</strong> al ente de control: <strong>{informe.entecontrol}</strong>.</p>
                        <p>Fecha límite: <strong>{fecha_entrega.strftime('%Y-%m-%d')}</strong></p>
                        <p>Recuerde que debe <strong>ENVIAR</strong> el ticket en la mesa de ayuda para que la oficina de <strong>INFORMATICA</strong> pueda validar la información <strong>A TIEMPO</strong>.</p> <br>
                        <p><a style="background: green; color: white; border-style: solid; border-width: 1px; border-color: white; padding: 5px; text-decoration: none; border-radius: 20px;" type="button" href="http://sara.imsalud.gov.co:8000/informe/entrega/{informe.id}">Ver informe</a> | <a style="background: green; color: white; border-style: solid; border-width: 1px; border-color: white; padding: 5px; text-decoration: none; border-radius: 20px;" type="button" href="https://soporte.imsalud.gov.co">Mesa de ayuda</a></p>
                    </body>
                    </html>
                """
                enviar_alarma2.apply_async(
                    args=[correo_responsable, mensaje_html, nombre_informe],
                    eta=fecha_alarma
                )
                
            if dias_anticipacion2 > 0:
                mensaje_html2 = f"""
                    <html>
                    <body>
                        <p><span>{nombre_responsable}</span>,</p>
                        <p>Está a <span style="color: green">{dias_anticipacion2} días</span> de la fecha LIMITE para entregar el informe: <strong>{informe.nombre}</strong> al ente de control: <strong>{informe.entecontrol}</strong>.</p>
                        <p>Fecha límite: <strong>{fecha_entrega.strftime('%Y-%m-%d')}</strong></p>
                        <p>Recuerde que debe <strong>ENVIAR</strong> el ticket en la mesa de ayuda para que la oficina de <strong>INFORMATICA</strong> pueda validar la información <strong>A TIEMPO</strong>.</p> <br>
                        <p><a style="background: green; color: white; border-style: solid; border-width: 1px; border-color: white; padding: 5px; text-decoration: none; border-radius: 20px;" type="button" href="http://sara.imsalud.gov.co:8000/informe/entrega/{informe.id}">Ver informe</a> | <a style="background: green; color: white; border-style: solid; border-width: 1px; border-color: white; padding: 5px; text-decoration: none; border-radius: 20px;" type="button" href="https://soporte.imsalud.gov.co">Mesa de ayuda</a></p>
                    </body>
                    </html>
                """
                enviar_alarma2.apply_async(
                    args=[correo_responsable, mensaje_html2, nombre_informe],
                    eta=fecha_alarma2
                )
                
            if dias_anticipacion3 > 0:
                mensaje_html3 = f"""
                    <html>
                    <body>
                        <p><span>{nombre_responsable}</span>,</p>
                        <p>Está a <span style="color: green">{dias_anticipacion3} días</span> de la fecha LIMITE para entregar el informe: <strong>{informe.nombre}</strong> al ente de control: <strong>{informe.entecontrol}</strong>.</p>
                        <p>Fecha límite: <strong>{fecha_entrega.strftime('%Y-%m-%d')}</strong></p>
                        <p>Recuerde que debe <strong>ENVIAR</strong> el ticket en la mesa de ayuda para que la oficina de <strong>INFORMATICA</strong> pueda validar la información <strong>A TIEMPO</strong>.</p> <br>
                        <p><a style="background: green; color: white; border-style: solid; border-width: 1px; border-color: white; padding: 5px; text-decoration: none; border-radius: 20px;" type="button" href="http://sara.imsalud.gov.co:8000/informe/entrega/{informe.id}">Ver informe</a> | <a style="background: green; color: white; border-style: solid; border-width: 1px; border-color: white; padding: 5px; text-decoration: none; border-radius: 20px;" type="button" href="https://soporte.imsalud.gov.co">Mesa de ayuda</a></p>
                    </body>
                    </html>
                """
                enviar_alarma2.apply_async(
                    args=[correo_responsable, mensaje_html3, nombre_informe],
                    eta=fecha_alarma3
                )
                
            # Actualizar la fecha de entrega para la siguiente iteración
            if periodicidadtipo == 'Dias':
                fecha_entrega += timedelta(days=periodicidad)
            elif periodicidadtipo == 'Meses':
                fecha_entrega += relativedelta(months=periodicidad)
            else:
                print(f"Tipo de periodicidad no reconocido: {periodicidadtipo}")
                break

        return redirect('informe')

    else:
        finformes = finforme()
        print("Renderizado")
    
    pertenece_a_informes = request.user.groups.filter(name='informes').exists()
    es_staff = request.user.is_staff
    return render(request, 'informes.html', {
        'entes_control': entes_control,
        'entes_dependencia': entes_dependencia,
        'finformes': finformes,
        'username': username,
        'pertenece_a_informes': pertenece_a_informes,
        'es_staff': es_staff
    })


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


@login_required
def listado(request):
    username = request.user.username
    es_staff = request.user.is_staff
    datos = informe.objects.all().select_related('entecontrol', 'dependencia')  # Para búsqueda relacionada en cascada

    # Añadir información sobre la entrega más reciente para cada informe
    informes_con_entrega_reciente = []
    now = timezone.now().date()
    for informe_obj in datos:
        entregas = entrega.objects.filter(informe=informe_obj, fecha__gt=now).order_by('fecha')
        entrega_reciente = entregas.first() if entregas.exists() else None
        informes_con_entrega_reciente.append({
            'informe': informe_obj,
            'entrega_reciente': entrega_reciente
        })

    # Ordenar los informes por entrega_reciente en forma ascendente
    informes_con_entrega_reciente = sorted(
        informes_con_entrega_reciente,
        key=lambda x: x['entrega_reciente'].fecha if x['entrega_reciente'] else timezone.datetime.max.date()
    )

    # Depuración: imprimir la lista ordenada
    for item in informes_con_entrega_reciente:
        entrega_fecha = item['entrega_reciente'].fecha if item['entrega_reciente'] else 'No hay entregas recientes'
        print(f"Informe ID: {item['informe'].id}, Fecha de entrega reciente: {entrega_fecha}")

    return render(request, 'listado.html', {
        'datos': informes_con_entrega_reciente,
        'username': username,
        'es_staff': es_staff
    })



 
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
def entregar(request, id):
    username = request.user.username
    informes = get_object_or_404(informe, id=id)

    dependencia = informes.dependencia
    responsable = ""
    correoresponsable = ""

    if dependencia:
        responsable = dependencia.responsable
        correoresponsable = dependencia.correoresponsable

    try:
        alarmas = alarma.objects.get(id=id)
        informe_id = alarmas.informe.id
        dias = alarmas.dias
    except alarma.DoesNotExist:
        dias = "No se encontraron alarmas"

    nombre = informes.nombre
    entregas = entrega.objects.filter(informe=informes).order_by('-fecha')
    now = timezone.now().date()
    entrega_reciente = entregas.filter(fecha__gt=now).order_by('fecha').first()

    entregas_con_evidencias = []
    for entrega_obj in entregas:
        evidencias = evidencia.objects.filter(entrega=entrega_obj)
        entregas_con_evidencias.append({
            'entrega': entrega_obj,
            'evidencias': evidencias
        })

    # Verifica si la última entrega tiene evidencias
    ultima_entrega = entregas.first() if entregas else None
    ultima_entrega_sin_evidencias = ultima_entrega and not evidencia.objects.filter(entrega=ultima_entrega).exists()

    # Determina si la entrega reciente tiene evidencias
    entrega_reciente_tiene_evidencias = False
    if entrega_reciente:
        entrega_reciente_tiene_evidencias = evidencia.objects.filter(entrega=entrega_reciente).exists()

    estado_pendiente = ''
    fechaentregapendiente = informes.fechaentregapendiente
    normativa = informes.normativa
    entecontrol = informes.entecontrol
    fechaentregainicial = informes.fechaentregainicial
    periodicidad = informes.periodicidad
    periodicidadtipo = informes.periodicidadtipo
    totalentregas = informes.totalentregas
    activo = informes.activo
    descripcion = informes.descripcion
    alarmas = informes.alarmas
    alarmas2 = informes.alarmas2
    alarmas3 = informes.alarmas3

    if request.method == 'POST':
        entrega_id = request.POST['entrega']
        nombre = request.POST['nombre']
        archivos = request.FILES.getlist('archivo')

        for archivo in archivos:
            evidencia_obj = evidencia(
                entrega_id=entrega_id,
                nombre=nombre,
                archivo=archivo
            )
            evidencia_obj.save()

        messages.success(request, 'Evidencias entregadas correctamente.')
        return redirect('entrega', id=id)

    es_staff = request.user.is_staff
    return render(request, 'entrega.html', {
        'nombre': nombre, 'normativa': normativa, 'entecontrol': entecontrol, 'dependencia': dependencia,
        'fechaentregainicial': fechaentregainicial, 'periodicidad': periodicidad, 'periodicidadtipo': periodicidadtipo,
        'totalentregas': totalentregas, 'activo': activo, 'descripcion': descripcion, 'dias': dias,
        'fechaentregapendiente': fechaentregapendiente, 'estado_pendiente': estado_pendiente, 'responsable': responsable,
        'correoresponsable': correoresponsable, 'entregas': entregas, 'entregas_con_evidencias': entregas_con_evidencias,
        'alarmas': alarmas, 'alarmas2': alarmas2, 'alarmas3': alarmas3, 'username': username, 'es_staff': es_staff,
        'entrega_reciente': entrega_reciente, 'ultima_entrega_sin_evidencias': ultima_entrega_sin_evidencias, 'now': now, 'id': id,
        'entrega_reciente_tiene_evidencias': entrega_reciente_tiene_evidencias
    })






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
    #####depedencias en la actualizacion#####
    dependencias = informes.dependencia
    responsable = ""
    correoresponsable = ""
    if dependencias:
        responsable = dependencias.responsable
        correoresponsable = dependencias.correoresponsable
    #####dependencias en la actualizacion####
    fechaentregainicial = informes.fechaentregainicial
    fechaentregapendiente = informes.fechaentregapendiente
    periodicidad = informes.periodicidad
    periodicidadtipo = informes.periodicidadtipo
    totalentregas = informes.totalentregas
    activo = informes.activo
    descripcion = informes.descripcion
    ####campos para ser actualizados###
    es_staff = request.user.is_staff
    alarmas = informes.alarmas
    alarmas2 = informes.alarmas2
    alarmas3 = informes.alarmas3
    ### inserccion del informe ##
    return render(request, 'informes-actualizar.html', {'nombre': nombre, 'entecontrols': entecontrols, 'dependencias': dependencias, 'descripcion': descripcion,
    'fechaentregainicial': fechaentregainicial, 'username': username, 'es_staff': es_staff, 'periodicidad': periodicidad, 'periodicidadtipo': periodicidadtipo,
    'totalentregas': totalentregas, 'responsable': responsable, 'correoresponsable': correoresponsable, 'alarmas': alarmas, 'alarmas2': alarmas2, 'alarmas3': alarmas3}) 

#opcion de eliminar aqui
@login_required
def informeeliminar(request, id):
    inform = informe.objects.get(id=id)
    inform.delete()
    return redirect('listado')
#opcion de eliminar aqui   