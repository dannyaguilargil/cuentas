from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
########################################
from django.http.response import JsonResponse
from django.http import JsonResponse
from gestion_usuarios.models import usolicitudes,usuario
from gestion_identidades.forms import Formidentidades,FormidentidadesSupervisor,FormidentidadesAdmin,FormidentidadesSupervisorRechazado,FormidentidadesRechazadoAdm,pazysalvosolicitud,pazysalvoaprobadoF,PazySalvoRechazado
from gestion_identidades.models import solicitudsistema,solicitudsistemasupervisor,aplicativo,modulo,solicitudsistemarechazado,pazysalvoaprobado
from gestion_identidades.models import pazysalvo
from django.contrib.auth.decorators import login_required, user_passes_test
from gestion_supervisor.models import supervisor
from gestion_informes.models import dependencia
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django import forms
from django.http import HttpResponse
from xhtml2pdf import pisa
from datetime import datetime

def staff_required(user):
    return user.is_staff 

@login_required
def identidades(request):
    username = request.user.username
    es_staff = request.user.is_staff
    es_supervisor = request.user.groups.filter(name='supervisor').exists()
    # Obtener el objeto usuario autenticado
    #usuario_obj = usuario.objects.filter(usuario=username).first()
    
    # Obtener todos los aplicativos para cargarlos en el formulario
    datos = aplicativo.objects.all()

    if request.method == 'POST':
        # Crear instancia del formulario con los datos enviados
        formularios = Formidentidades(request.POST)
        
        if formularios.is_valid():
            # Guardar el formulario si es válido
            formularios.save()
            messages.success(request, 'La solicitud se ha enviado al supervisor.')
            return redirect('identidades')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos ingresados.')
    else:
        # Crear un formulario vacío inicializando con los datos del usuario autenticado
        formularios = Formidentidades(initial={
           
        })

    try:
        usuario_detalle = usuario.objects.get(usuario=request.user)
    except Usuario.DoesNotExist:
        usuario_detalle = None

    # Renderizar la plantilla con el formulario y los datos del usuario autenticado
    return render(request, 'identidades.html', {
        'username': username,
        'formularios': formularios,
        'datos': datos,
        'es_staff': es_staff,
        'es_supervisor': es_supervisor,
        'usuario': usuario_detalle, 
    })


@login_required
def pazysalvos(request):
    username = request.user.username
    es_staff = request.user.is_staff
    es_supervisor = request.user.groups.filter(name='supervisor').exists()

    # Obtén el objeto 'usuario' asociado al usuario autenticado
    user_instance = usuario.objects.filter(usuario=request.user).first()
    # Verifica si el usuario tiene un registro aprobado
    aprobado = pazysalvoaprobado.objects.filter(usuario=user_instance, permisos=True, rfid=True).exists()

    if request.method == 'POST':
        form = pazysalvosolicitud(request.POST)
        if form.is_valid():
            form.save()  # Guardar el formulario si es válido
            messages.success(request, 'Paz y salvo solicitado al administrador!, en caso de ser aceptado se notificara por correo')
            return redirect('pazysalvo')  # Cambia esto por el nombre de la vista correspondiente

    else:
        form = pazysalvosolicitud()
        if user_instance:
            form.fields['usuario'].initial = user_instance  # Establecer el usuario autenticado como valor inicial
            form.fields['usuario'].widget = forms.HiddenInput()
            form.fields['permisos'].required = True 
            form.fields['rfid'].required = True 
 
    pdf_url = None
    if aprobado and user_instance:
        # Genera la URL del PDF usando la cédula
        cedula = user_instance.cedula  # Asegúrate de que este campo exista en tu modelo
        pdf_url = f'certificado/{cedula}'
      

    return render(request, 'pazysalvo.html', {
        'username': username,
        'es_staff': es_staff,
        'es_supervisor': es_supervisor,
        'form': form,  # Pasar el formulario al template
        'aprobado': aprobado,
        'pdf_url': pdf_url if aprobado else None,
        'messages': messages.get_messages(request),
        #'fecha_creacion': fecha_creacion
    })

@login_required
def usolicitud(request):
    usuarios = list(solicitudsistema.objects.values())
    data = {'solicitud': usuarios}
    return JsonResponse(data)

def listadmin(request):
    usuarios = list(solicitudsistemasupervisor.objects.values())
    data = {'solicitud': usuarios}
    return JsonResponse(data)

@login_required
def identidadespendientes(request):
    datos = solicitudsistema.objects.values()
    datosapp = aplicativo.objects.all()
    datosmod = modulo.objects.all()
    datosdep = dependencia.objects.all()
    datossup = supervisor.objects.all()#pendiente validar sino lo oculto y lo hago con id
    username = request.user.username
    es_staff = request.user.is_staff
    es_supervisor = request.user.groups.filter(name='supervisor').exists()
    
    if request.method == 'POST':
        if request.POST.get('aprobar') == 'aprobar':
            form = FormidentidadesSupervisor(request.POST)
            if form.is_valid():
            # Guarda el nuevo registro
                form.save()
                #messages.success(request, 'Aplicativo aprobado, se notificará al administrador')
                #aqui debe eliminar la solicitud
                solicitud_id = form.cleaned_data.get('id')
                
                 # Intentar obtener y eliminar la solicitud
                try:
                    solicitud = solicitudsistema.objects.get(id=solicitud_id)
                    solicitud.delete()
                    messages.success(request, 'Solicitud APROBADA correctamente, se notificará al ADMINISTRADOR')
                except solicitudsistema.DoesNotExist:
                    messages.error(request, 'La solicitud no existe.')
                except Exception as e:
                    messages.error(request, f'Error al eliminar la solicitud: {str(e)}')
                 #notificar por correo
                return redirect('identidadespendientes')
              

        elif request.POST.get('rechazar') == 'rechazar':
              form = FormidentidadesSupervisorRechazado(request.POST)
              if form.is_valid():
                 form.save()
                 #messages.error(request, 'Aplicativo rechazado, se notificará por correo al usuario')
                 # Obtener el ID de la solicitud para eliminar
                 solicitud_id = form.cleaned_data.get('id')
                
                 # Intentar obtener y eliminar la solicitud
                 try:
                    solicitud = solicitudsistema.objects.get(id=solicitud_id)
                    solicitud.delete()
                    messages.error(request, 'Solicitud RECHAZADA correctamente, se notificará al correo al asociado.')
                 except solicitudsistema.DoesNotExist:
                    messages.error(request, 'La solicitud no existe.')
                 except Exception as e:
                    messages.error(request, f'Error al eliminar la solicitud: {str(e)}')
                 #notificar por correo
                 return redirect('identidadespendientes')

    else:
        form = FormidentidadesSupervisor()
    return render(request, 'pendientes.html', {'datos': datos, 'foripendiente': form, 'username': username, 'datosapp': datosapp, 'datosmod': datosmod, 'datossup': datossup, 'datosdep': datosdep, 'es_staff': es_staff
                 ,'es_supervisor': es_supervisor})

@login_required
@user_passes_test(staff_required)
def identidadespendientesadmin(request):
    username = request.user.username
    datos = solicitudsistemasupervisor.objects.all()  # Cambia según tu modelo
    datosapp = aplicativo.objects.all()
    datosmod = modulo.objects.all()
    datosdep = dependencia.objects.all()
    datossup = supervisor.objects.all()  # Pendiente validar si no lo oculto y lo hago con id
    datosu = usolicitudes.objects.values()  # Solicitudes de usuario
    combined_data = list(datos) + list(datosu)
    es_staff = request.user.is_staff
    es_supervisor = request.user.groups.filter(name='supervisor').exists()

    if request.method == 'POST':
        if request.POST.get('aprobar') == 'aprobar':
            forma = FormidentidadesAdmin(request.POST)
        
            if forma.is_valid():
                forma.save()
                
                solicitud_id = forma.cleaned_data.get('id')
                cedula = forma.cleaned_data.get('cedula')
              
                try:
                    if solicitud_id:
                        solicitud = solicitudsistemasupervisor.objects.get(id=solicitud_id)
                    else:
                        solicitud = usolicitudes.objects.get(cedula=cedula)
                        ###AQUI VA EL PROCESO DE LA CREACION DE USUARIO
                        username = forma.cleaned_data.get('usuario')
                        email = forma.cleaned_data.get('email')
                        password = forma.cleaned_data.get('contrasena')
                        ####queda pendiente el tema del nombre####
                        new_user = User.objects.create_user(username=username, email=email, password=password)
                        new_user.save()
                        user = authenticate(username=username, password=password)
                        try:
                            grupo = Group.objects.get(name='identidades')
                            grupo.user_set.add(new_user)  # Agrega el usuario al grupo
                        except Group.DoesNotExist:
                            print("El grupo no existe.")
                            ###AQUI VA EL PROCESO DE LA CREACION DE USUARIO

                    ##validar para recibir aplicativo y modulo##
                    ###Envío de correo electrónico##########
                    email = forma.cleaned_data.get('email')
                    usuario = forma.cleaned_data.get('usuario')
                    contrasena = forma.cleaned_data.get('contrasena')
                    subject = "Bienvenido a SARA - imsalud "
                    message = f"""
                    <html>
                    <body>
                        <p>Tu cuenta ha sido creada exitosamente con el usuario: <strong>{usuario}</strong> y contraseña: <strong>{contrasena}</strong>.</p>
                        <p>
                            <a style="background: green; color: white; border-style: solid; border-width: 1px; border-color: white; padding: 5px; text-decoration: none; border-radius: 20px;" 
                            href="http://sara.imsalud.gov.co:8000/login">Ingresar a SARA</a>
                        </p>
                    </body>
                    </html>
                    """
                    sender = "noreply@imsalud.gov.co"
                    recipient_list = [email]
                    send_mail(
                        subject,
                        message,  # El mensaje en texto plano
                        sender,
                        recipient_list,
                        fail_silently=False,
                        html_message=message  # Aquí es donde se agrega el contenido HTML
                    )
                    ####envio de correo electronico#############
                    solicitud.delete()
                    messages.success(request, 'Solicitud APROBADA correctamente, se notificara al correo al asociado.')
                    ### AQUI VOY A REALIZAR LA CREACION DEL USUARIO#####
                    ###AQUI VA EL USER###
                    usuario = forma.cleaned_data.get('usuario')

                except (solicitudsistemasupervisor.DoesNotExist, usolicitudes.DoesNotExist):
                    messages.error(request, 'La solicitud no existe.')
                except Exception as e:
                    messages.error(request, f'Error al eliminar la solicitud: {str(e)}')
                return redirect('identidadespendientesadmin')

            else:
                #print(forma.errors)  # Mostrar errores en la consola
                #print(request.POST)
                messages.error(request, 'Error en el formulario. Verifique los datos.')


        elif request.POST.get('rechazar') == 'rechazar':
            forma = FormidentidadesRechazadoAdm(request.POST)

            if forma.is_valid():
                forma.save()
                #messages.error(request, 'Aplicativo rechazado, se notificará por correo al usuario')

                # Obtener el ID de la solicitud para eliminar
                solicitud_id = forma.cleaned_data.get('id')
                cedula = forma.cleaned_data.get('cedula')
                ####en caso no haber id que me tome la cedula
             
                try:
                    if solicitud_id:
                        solicitud = solicitudsistemasupervisor.objects.get(id=solicitud_id)
                    #####LO QUE VA EN EL ELSE
                    else:
                        solicitud = usolicitudes.objects.get(cedula=cedula)
                        print("rechazado")
                    
                    print("dentro del try")
                    solicitud.delete()
                    messages.error(request, 'Solicitud RECHAZADA correctamente, se notificara al correo al asociado.')
                except (solicitudsistemasupervisor.DoesNotExist, usolicitudes.DoesNotExist):
                    messages.error(request, 'La solicitud no existe.')
                except Exception as e:
                    messages.error(request, f'Error al eliminar la solicitud: {str(e)}')
                return redirect('identidadespendientesadmin')
            else:
                #print(forma.errors)  # Mostrar errores en la consola
                #print(request.POST)
                messages.error(request, 'Error en el formulario. Verifique los datos.')

        else:
            messages.error(request, 'Error al procesar el formulario.')

    else:
        forma = FormidentidadesAdmin()

    return render(request, 'pendientesadmin.html', {
        'datos': combined_data,
        'form': forma,
        'username': username,
        'datosapp': datosapp,
        'datosmod': datosmod,
        'datosdep': datosdep,
        'datossup': datossup,
        'es_staff': es_staff,
        'es_supervisor': es_supervisor
    })


@login_required
def pazysalvohtml(request):
    nombre = ""
    return render(request, 'pazysalvohtml.html', {'nombre': nombre})
    
@login_required    
def certificado(request,cedula):
    nombre = "" 
    segundonombre = " "
    primerapellido = " "
    segundoapellido = " "
    fechafinalcontrato = ""
    auxc = ""
    cargo = " " 
    usuario_obj = usuario.objects.filter(cedula=cedula).first()
    if usuario.objects.filter(cedula=cedula).exists():
        nombre = usuario_obj.nombre
        segundonombre = usuario_obj.segundonombre
        primerapellido = usuario_obj.primerapellido  
        segundoapellido = usuario_obj.segundoapellido
        auxc = usuario_obj.cedula 
        fechafinalcontrato = usuario_obj.fechafinalcontrato 
        cargo = usuario_obj.cargo

    context = {'nombre': nombre, 'segundonombre': segundonombre, 'primerapellido': primerapellido, 'segundoapellido': segundoapellido , 'cedula': auxc, 'fechafinalcontrato': fechafinalcontrato, 'cargo': cargo}
    template = render(request, 'pazysalvohtml.html', context)

    # Crear un objeto HttpResponse con tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificadopazysalvo.pdf"'
    # conversion xhtml a pdf
    pisa_status = pisa.CreatePDF(template.content, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Ocurrió un error al generar el PDF')
    return response

###listado de informe ###
@login_required
def listadoaplicativos(request):
    aps = list(aplicativo.objects.values())
    data = {'aps': aps}
    return JsonResponse(data)

@login_required
def listadomodulos(request):
    aplicativo_id = request.GET.get('aplicativo_id')
    if aplicativo_id:
        mods = list(modulo.objects.filter(aplicativo_id=aplicativo_id).values('id', 'nombre'))
        data = {'modulos': mods}
    else:
        data = {'modulos': []}
    return JsonResponse(data)

@login_required
def solicitudespaz(request):
    # Obtiene los datos de pazysalvo, incluyendo el nombre del usuario
    aps = list(pazysalvo.objects.values(
        'id', 
        'usuario__nombre',  
        'usuario__segundonombre', 
        'usuario__primerapellido', 
        'usuario__segundoapellido', 
        'permisos', 
        'rfid', 
        'fecha_creacion', 
        'fecha_actualizacion'
    ))
    data = {'pazysalvo_solicitudes': aps}
    return JsonResponse(data)

@login_required
@user_passes_test(staff_required)
def pazysalvolistado(request):
    username = request.user.username
    datos = pazysalvo.objects.all()  # Cambia según tu modelo
    datosapp = aplicativo.objects.all()
    datosmod = modulo.objects.all()
    datosdep = dependencia.objects.all()
    datossup = supervisor.objects.all()
    es_staff = request.user.is_staff

    if request.method == 'POST':
        if 'aprobar' in request.POST:
            forma = pazysalvoaprobadoF(request.POST)
            if forma.is_valid():
                forma.save()
                solicitud_id = forma.cleaned_data.get('id')
                try:
                    solicitud = pazysalvo.objects.get(id=solicitud_id)
                    #nuevo_pazysalvo.usuario = solicitud.usuario  # Asumiendo que tienes este campo en el modelo
                    #nuevo_pazysalvo.save()  # Guarda la nueva solicitud aprobada
                    solicitud.delete()  # Elimina la solicitud original
                    messages.success(request, 'Paz y salvo APROBADO, se notificará al correo asociado.')
                except pazysalvo.DoesNotExist:
                    messages.error(request, 'La solicitud de paz y salvo no existe.')
                except Exception as e:
                    messages.error(request, f'Error al procesar la aprobación: {str(e)}')
                return redirect('pazysalvolistado')

            else:
                messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos ingresados.')
                return redirect('pazysalvolistado')

        elif 'rechazar' in request.POST:
            forma = PazySalvoRechazado(request.POST)

            if forma.is_valid():
                forma.save()
                solicitud_id = forma.cleaned_data.get('id')

                try:
                    if solicitud_id:
                         solicitud = pazysalvo.objects.get(id=solicitud_id)
                    solicitud.delete()
                    messages.error(request, 'Solicitud RECHAZADA, se notificará al correo asociado.')
                except pazysalvo.DoesNotExist:
                    messages.error(request, 'La solicitud no existe.')
                except Exception as e:
                    messages.error(request, f'Error al eliminar la solicitud: {str(e)}')

                return redirect('pazysalvolistado')

        else:
            messages.error(request, 'Error al procesar el formulario.')

    else:
        forma = PazySalvoRechazado()

    return render(request, 'pazysalvolistado.html', {
        'datos': datos,
        'form': forma,
        'username': username,
        'datosapp': datosapp,
        'datosmod': datosmod,
        'datosdep': datosdep,
        'datossup': datossup,
        'es_staff': es_staff
    })

@login_required
def identidadesperfil(request):
    username = request.user.username
    es_staff = request.user.is_staff
    # Obtener el objeto usuario autenticado
    usuario_obj = usuario.objects.filter(usuario=username).first()
    
    # Obtener todos los aplicativos para cargarlos en el formulario
    datos = aplicativo.objects.all()

    if request.method == 'POST':
        # Crear instancia del formulario con los datos enviados
        formularios = Formidentidades(request.POST)
        
        if formularios.is_valid():
            # Guardar el formulario si es válido
            formularios.save()
            messages.success(request, 'La solicitud se ha enviado al supervisor.')
            return redirect('identidadesperfil')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos ingresados.')
    else:
        # Crear un formulario vacío inicializando con los datos del usuario autenticado
        formularios = Formidentidades(initial={
            #'nombre': usuario_obj.nombre,
            #'segundonombre': usuario_obj.segundonombre,
            #'primerapellido': usuario_obj.primerapellido,
            #'segundoapellido': usuario_obj.segundoapellido,
            #'cargo': usuario_obj.cargo,
            #'email': usuario_obj.email,
            #'cedula': usuario_obj.cedula,
            #'supervisor': usuario_obj.supervisor,
        })

    # Renderizar la plantilla con el formulario y los datos del usuario autenticado
    return render(request, 'identidadesperfil.html', {
        'username': username,
        'formularios': formularios,
        'datos': datos,
        'es_staff': es_staff
    })

@login_required
def acuerdoc(request):
    nombre = ""
    return render(request, 'acuerdochtml.html', {'nombre': nombre})

@login_required
def tratamiento(request):
    nombre = ""
    fecha_actual = datetime.now().date() 
    return render(request, 'tratamientohtml.html', {'nombre': nombre, 'fecha_actual': fecha_actual})

@login_required    
def tratamientodp(request,cedula):
    nombre = "" 
    fecha_actual = datetime.now().date() 
    #segundonombre = " "
    #primerapellido = " "
    #segundoapellido = " "
    #fechafinalcontrato = ""
    #auxc = ""
    #cargo = " " 
    usuario_obj = usuario.objects.filter(cedula=cedula).first()
    if usuario.objects.filter(cedula=cedula).exists():
        nombre = usuario_obj.nombre
        segundonombre = usuario_obj.segundonombre
        primerapellido = usuario_obj.primerapellido  
        segundoapellido = usuario_obj.segundoapellido
        cedula = usuario_obj.cedula 
        email = usuario_obj.email 
        #celular = usuario_obj.celular

    context = {'nombre': nombre, 'segundonombre': segundonombre, 'primerapellido': primerapellido, 'segundoapellido': segundoapellido, 'cedula': cedula, 'email': email, 'fecha_actual': fecha_actual }
    template = render(request, 'tratamientohtml.html', context)

 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="tratamientodatospersonales.pdf"'

    pisa_status = pisa.CreatePDF(template.content, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Ocurrió un error al generar el PDF')
    return response
