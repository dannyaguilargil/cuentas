
from django.shortcuts import render, redirect
#para el uso de datatables
from django.http.response import JsonResponse
from gestion_usuarios.models import usuario
from gestion_usuarios.models import usolicitudes
from gestion_usuarios.models import cuentausuario
from gestion_usuarios.models import prueba
from gestion_usuarios.models import contrato,rp,actainicio
from gestion_usuarios.forms import Users
from gestion_usuarios.forms import Usuario
from gestion_usuarios.forms import Contrato, Rp, Actainicio, Planilla, Actividades, Actapago, Certificadoseguimiento, Cusuario
from django.contrib import messages
#gestion del usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#def  usuarios(request):
#     return render(request, 'C:/xampp/htdocs/sistemas_cuentas/gestion_usuarios/templates/index.html')

def  base(request):
     return render(request, 'base_layout_usuarios.html') #archivo base de usuarios

def  usuarios(request):
     username = request.user.username #validar esto
     return render(request, 'usuarios.html', {'username': username}) # se modifica esto con lo anterior pero para no poner toda la ruta, cambiando en settin.py insatllerds app poniendo la ruta

################LOGIN####################
def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_staff:
                     login(request, user)
                     return redirect('usuarios')
                else:
                     login(request, user)
                     return redirect('perfil')
            else:
                messages.error(request, 'Las credenciales de inicio de sesión son inválidas.')
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})
################LOGIN####################

#Aqui hago insercciones
def solicitud_usuario(request):
    #Aqui va el formulario dinamico
    formulario = Users(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, ' Cuenta creada')
        return render(request, 'solicitud.html')
    return render(request, 'solicitud.html', {'formulario': formulario})
#aqui hago insecciones



#GESTION DE DOCUMENTOS DE GESCON
def documentos(request):
    form = Contrato(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    formrp = Rp(request.POST or None)
    if formrp.is_valid():
        formrp.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    forminicio = Actainicio(request.POST or None)
    if forminicio.is_valid():
        forminicio.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    return render(request, 'sdocumentos.html', {'form': form, 'formrp': formrp, 'forminicio': forminicio})
#GESTION DE DOCUMENTOS GESCON

#############TRAE DATOS SEGUN CORRESPONDE ###################
#solo usuarios autenticados
#@login_required
#usuarios = usuario.objects.all()  ##aqui se trae todo los campos de usuario
#usuarios = usuario.objects.filter(usuario='username')
#usuarios = usuario.objects.all().values('usuario')
#usuarios = usuario.objects.filter(usuario='IMSALUD').values_list('nombre', flat=True)
#usuarios = usuario.objects.filter(usuario=username).first().nombre  #trae el dato especifico que quiero
#####################VALIDANDO CONSULTAS #######################
def perfil(request):
    formperfil = Cusuario(request.POST or None)
    username = request.user.username
    usuario_obj = usuario.objects.filter(usuario=username).first()
    progreso=1
    if usuario.objects.filter(usuario=username).exists():
        nombre_usuario = usuario_obj.nombre
        segundo_nombre = usuario_obj.segundonombre #HASTA AQUI VA BIEN
        primer_apellido = usuario_obj.primerapellido
        segundo_apellido = usuario_obj.segundoapellido
        cedula = usuario_obj.cedula
        estado = "CREADO"
        email = usuario_obj.email
        supervisor = usuario_obj.supervisor
        progreso=10
        ###########GESTION DE CONTRATACION########################
        usuario_obj2 = contrato.objects.filter(usuario_id=cedula).first()
        if contrato.objects.filter(usuario_id=cedula).exists():
            numero = usuario_obj2.numero
            objeto = usuario_obj2.objeto
            valor = usuario_obj2.valor
            fechaterminacion = usuario_obj2.fechaterminacion
            duracion = usuario_obj2.duracion
            progreso=20
            ###########GESTION DE CONTRATACION RP########################  
            usuario_obj3 = rp.objects.filter(usuario_id=cedula).first()
            if rp.objects.filter(usuario_id=cedula).exists():
                numerorp = usuario_obj3.numero
                fecharp = usuario_obj3.fecha
                progreso=30
                ###########GESTION DE CONTRATACION ACTA INICIO########################  
                usuario_obj4 = actainicio.objects.filter(usuario_id=cedula).first()
                if actainicio.objects.filter(usuario_id=cedula).exists():
                    numeroai = usuario_obj4.numero
                    fechaai = usuario_obj4.fecha
                    progreso=40
    else:
        nombre_usuario = "No tiene nombre creado"
        segundo_nombre = ""
        primer_apellido = "No ha creado apellido"
        segundo_apellido = ""
        cedula = "No tiene cedula creada"
        estado = "No ha cargado documentos"
        email = "No tiene email creado"
        supervisor = "No tiene supervisor asignado"
        numero = "No tiene contrato asignado"
        objeto = "No tiene contrato asignado"
        valor = "No tiene contrato asignado"
        fechaterminacion = "No tiene contrato asignado"
        duracion = "No tiene contrato asignado"
        numerorp = "No tiene registro presupuetal asignado"
        fecharp = "No tiene registro presupuetal asignado"
        numeroai = "No tiene acta de inicio asignado"
        fechaai = "No tiene acta de inicio asignado"
        
    if formperfil.is_valid():
        formperfil.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
        #' datos_usuario': datos_usuario}
    return render(request, 'perfil.html', {'formperfil': formperfil, 'username': username, 'nombre_usuario': nombre_usuario, 'segundo_nombre': segundo_nombre, 'primer_apellido': primer_apellido, 'segundo_apellido': segundo_apellido, 'cedula': cedula, 'estado': estado, 'email': email,
                                        'supervisor': supervisor, 'numero': numero, 'objeto': objeto, 'valor': valor, 'fechaterminacion': fechaterminacion, 'duracion': duracion, 'numerorp': numerorp, 'fecharp': fecharp, 'numeroai': numeroai, 'progreso': progreso, 'fechaai': fechaai})
#############TRAE DATOS SEGUN CORRESPONDE ###################
    
#gestion de documentos de usuarios
def documentos_usuario(request):
    form = Contrato(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    formrp = Rp(request.POST or None)
    if formrp.is_valid():
        formrp.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    forminicio = Actainicio(request.POST or None)
    if forminicio.is_valid():
        forminicio.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    formplanilla = Planilla(request.POST or None)
    if formplanilla.is_valid():
        formplanilla.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    formactividades = Actividades(request.POST or None)
    if formactividades.is_valid():
        formactividades.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    formactapago = Actapago(request.POST or None)
    if formactapago.is_valid():
        formactapago.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    formcertificadoseguimiento = Certificadoseguimiento(request.POST or None)
    if formcertificadoseguimiento.is_valid():
        formcertificadoseguimiento.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos.html')
    return render(request, 'sdocumentos_usuario.html', {'form': form, 'formrp': formrp, 'forminicio': forminicio, 'formplanilla': formplanilla, 'formactividades': formactividades, 'formactapago': formactapago, 'formcertificadoseguimiento': formcertificadoseguimiento})
#gestion de documentos de usuarios

def list_usuarios(request):
    usuarios = list(usuario.objects.values())
    data = {'usuarios': usuarios}
    return JsonResponse(data)


def usuarios_pendientes(request):
    return render(request, 'usuariospendientes.html')

#opcion de eliminar aqui
def eliminar(request, cedula):
    usolicitudes = usolicitudes.objects.get(cedula=cedula)
    usolicitudes.delete()
    return redirect('usuarios')
#opcion de eliminar aqui   

def usolicitud(request):
    usuarios = list(usolicitudes.objects.values())
    data = {'usuarios': usuarios}
    return JsonResponse(data)

#logueo de usuario
#AQUI VOY A INTENTAR CREAR EL USUARIO EN AUTH_USER PARA DARLE LA SEGURIDAD#
def crear(request):
    formularios = Usuario(request.POST or None)
    if formularios.is_valid():
        formularios.save()
        #aqui voy a insertar en auth_user
        username = formularios.cleaned_data.get('usuario')
        email = formularios.cleaned_data.get('email')
        password = formularios.cleaned_data.get('contrasena')
         # Crear un nuevo usuario
        new_user = User.objects.create_user(username=username, email=email, password=password)
        # Guardar el nuevo usuario
        new_user.save()
        #autenticar el usuario
        user = authenticate(username=username, password=password)
        messages.success(request, 'Cuenta creada')
        return render(request, 'crear.html')
    return render(request, 'crear.html',  {'formularios': formularios})

#logout de la pagina
def logout(request):
    logout(request)
    return redirect('inicio')
