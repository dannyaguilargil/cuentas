from django.shortcuts import render,redirect
from django.contrib import messages
########################################
from django.http.response import JsonResponse
from django.http import JsonResponse
from gestion_usuarios.models import usolicitudes,usuario
from gestion_identidades.forms import Formidentidades,FormidentidadesSupervisor
from gestion_identidades.models import solicitudsistema,solicitudsistemasupervisor
from django.contrib.auth.decorators import login_required

@login_required
def identidades(request):
    username = request.user.username
    ### para llenar el campo de formato de identidades #####
    usuario_obj = usuario.objects.filter(usuario=username).first()
    #if usuario.objects.filter(usuario=username).exists():
    #    cedula = usuario_obj.cedula
    ####para realizar la inserccion del formato de identidades ####
    if request.method == 'POST':
        formularios = Formidentidades(request.POST)
        if formularios.is_valid():
            formularios.save()
            messages.success(request, 'La solicitud se ha enviado al supervisor.')
            return redirect('identidades')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos ingresados.')

    else:
        formularios = Formidentidades()

     ####para realizar la inserccion del formato de identidades ####
    return render(request, 'identidades.html' , {'username': username, 'formularios': formularios})

@login_required
def pazysalvo(request):
    return render(request, 'pazysalvo.html')

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
    ##### aqui va el registro de la identidad
    foripendiente = FormidentidadesSupervisor(request.POST or None)
    if foripendiente.is_valid():
        foripendiente.save()
        messages.success(request, 'Usuario registrado con exito')
        ###AQUI DEBO ELIMINAR LA SOLICITUD UNA VEZ REGISTRADO###
        #if user is not None:
        #    solicitud_obj = usolicitudes.objects.get(cedula=cedula)
        #    solicitud_obj.delete()
    return render(request, 'pendientes.html', {'datos': datos, 'foripendiente': foripendiente})

@login_required
def identidadespendientesadmin(request):
    #solicitud_obj = ""
    datos = solicitudsistemasupervisor.objects.values()
    return render(request, 'pendientesadmin.html', {'datos': datos})

@login_required
def pazysalvohtml(request):
    nombre = ""
    return render(request, 'pazysalvohtml.html', {'nombre': nombre})
    
    #SELECT count(*) from gestion_usuarios_contrato where usuario_id=1090492324;
    
def certificado(request,cedula):
    nombre = "" #Lo remplazo con el que traiga del modelo
#    segundonombre = ""
#    primerapellido = ""
#    segundoapellidos = ""
#    numerocontratos = ""
#    numeroproceso = ""
    aux = cedula
#    supervisor = ""
#    objetocontrato = ""
#    fechaperfeccionamientos = ""
#    duracion = ""
#    dependenciausuario = ""
#    duracioncontrato = ""
#    numerorp = ""
#    fechacontrato = ""
#    fechaterminacion = ""
#    valorpagar = 1
#    numeroplanilla = ""
#    nombresalud = ""
#    valorsalud = ""
#    nombrepension = ""
#    valorpension = ""
#    nombrearl = ""
#    valorarl = ""
#    numerocuentabancaria = ""
#    tipocuenta = ""
#    nombrecb = ""
#    nombre_mes = ""
#    dia = ""
#    año = ""
#    valorcontrato = ""
#    cuenta = 1 #remplazar por el numero de cuenta recibida
    ##############EXTRACCION DE DATOS APARTIR DE LA CEDULA############
#    usuario_obj = usuario.objects.filter(cedula=cedula).first()
#    if usuario.objects.filter(cedula=cedula).exists():
#         nombre = usuario_obj.nombre
#         segundonombre = usuario_obj.segundonombre
#         primerapellido = usuario_obj.primerapellido
#         segundoapellidos = usuario_obj.segundoapellido
#         dependenciausuario = usuario_obj.dependencia
#         usuario_obj2 = contrato.objects.filter(usuario_id=cedula).first()
#         if contrato.objects.filter(usuario_id=cedula).exists():
#            numerocontratos = usuario_obj2.numero
#            numeroproceso = usuario_obj2.numeroproceso
#            fechaperfeccionamientos = usuario_obj2.fechaperfeccionamiento
#            fechacontrato = usuario_obj2.fechacontrato
#            supervisor = usuario_obj2.supervisor
#            archivo = usuario_obj2.archivo
#            #archivo2 = archivo.replace('contratista', 'static')
#            objetocontrato = usuario_obj2.objeto
#            valorcontrato = usuario_obj2.valor
#            fechaterminacion = usuario_obj2.fechaterminacion
#            duracioncontrato = usuario_obj2.duracion
#            cuenta = 1
#            usuario_obj3 = rp.objects.filter(usuario_id=cedula).first()
#            if rp.objects.filter(usuario_id=cedula).exists():
#                  numerorp = usuario_obj3.numero
#                  usuario_obj4 = planilla.objects.filter(usuario_id=cedula).first()
#                  if planilla.objects.filter(usuario_id=cedula).exists():
#                      numeroplanilla = usuario_obj4.numero
#                      nombresalud = usuario_obj4.nombresalud
#                      valorsalud = usuario_obj4.valorsalud
#                      nombrepension = usuario_obj4.nombrepension
#                      valorpension = usuario_obj4.valorpension
#                      nombrearl = usuario_obj4.nombrearl
#                      valorarl = usuario_obj4.valorarl
#                      usuario_obj5 = cuentabancaria.objects.filter(usuario_id=cedula).first()
#                      if cuentabancaria.objects.filter(usuario_id=cedula).exists():
#                          numerocuentabancaria = usuario_obj5.numero
#                          tipocuenta = usuario_obj5.tipocuenta
#                          nombrecb = usuario_obj5.nombrecb
#                          fecha_actual = datetime.now()
#                          locale.setlocale(locale.LC_TIME, 'es_ES')
#                          nombre_mes = fecha_actual.strftime('%B')
#                          #mes = fecha_actual.month
#                          dia = fecha_actual.day
#                          año = fecha_actual.year
                          # Establecer el idioma en español
                      
                      
    context = {'nombre': nombre}
    template = render(request, 'pazysalvohtml', context)