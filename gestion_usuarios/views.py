
from django.shortcuts import render, redirect
#para el uso de datatables
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from gestion_usuarios.models import usuario
from gestion_usuarios.models import usolicitudes
from gestion_usuarios.models import cuentausuario
from gestion_usuarios.models import prueba
from gestion_usuarios.models import contrato,rp,actainicio,planilla
from gestion_usuarios.models import actividades,actapago,certificadoseguimiento
from gestion_usuarios.forms import Users
from gestion_usuarios.forms import Usuario, InsertForm, InsertFormU, InsertFormUE
from gestion_usuarios.forms import Contrato, Rp, Actainicio, Planilla, Actividades, Actapago, Certificadoseguimiento, Cusuario,Contratou
from django.contrib import messages
#gestion del usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django_datatables_view.base_datatable_view import BaseDatatableView

#def  usuarios(request):
#     return render(request, 'C:/xampp/htdocs/sistemas_cuentas/gestion_usuarios/templates/index.html')

def  base(request):
     return render(request, 'base_layout_usuarios.html') #archivo base de usuarios

def  usuarios(request):
     datosu = usuario.objects.values()
     username = request.user.username #validar esto
     return render(request, 'usuarios.html', {'username': username, 'datosu': datosu}) # se modifica esto con lo anterior pero para no poner toda la ruta, cambiando en settin.py insatllerds app poniendo la ruta

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
                     return redirect('ops')
            else:
                messages.error(request, 'Las credenciales de inicio de sesión son inválidas.')
                return redirect('inicio')
    else:
        form = AuthenticationForm()
        #messages.error(request, 'Las credenciales de inicio de sesión son inválidas.')
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
    form = Contrato(request.POST ,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Documento cargado')
        return render(request, 'sdocumentos.html')
    formrp = Rp(request.POST or None)
    if formrp.is_valid():
        formrp.save()
        messages.success(request, 'Documento cargado')
        return render(request, 'sdocumentos.html')
    forminicio = Actainicio(request.POST or None)
    if forminicio.is_valid():
        forminicio.save()
        messages.success(request, 'Documento cargado')
        return render(request, 'sdocumentos.html')
    return render(request, 'sdocumentos.html', {'form': form, 'formrp': formrp, 'forminicio': forminicio})
#GESTION DE DOCUMENTOS GESCON

#############TRAE DATOS SEGUN CORRESPONDE ###################
#solo usuarios autenticados
#@login_required
#####################VALIDANDO CONSULTAS #######################
def perfil(request):
       ################# AQUI VOY A REGISTRAR LA CUENTA######
    ### username = formularios.cleaned_data.get('usuario')##
    formper = InsertForm(request.POST or None)
    if formper.is_valid():
        formper.save()
        #email = formper.cleaned_data.get('email')
        #cedula = formper.cleaned_data.get('cedula')
        #cuenta = cuentausuario(email=email, cedula=cedula)
        #cuenta.save()
        return redirect('perfil')
            #else:
            #    formp = InsertForm()
            ################# AQUI VOY A REGISTRAR LA CUENTA######     
    username = request.user.username
    usuario_obj = usuario.objects.filter(usuario=username).first()
    progreso=1
    ###### SI ESTA CREADO CON EL ADMIN SI CARGA Y VALIDA###########
    #######CUANDO EL USUARIO ESTA CREADO Y NO TIENE DOCUMENTOS NO CARGA
    numero = 2
    objeto = "No tiene contrato asignado"
    valor = "No tiene contrato asignado"
    fechaterminacion = "No tiene contrato asignado"
    duracion = "No tiene contrato asignado"
    numerorp = "No tiene registro presupuetal asignado"
    fecharp = "No tiene registro presupuetal asignado"
    numeroai = "No tiene acta de inicio asignado"
    fechaai = "No tiene acta de inicio asignado"
    numeroplanilla = "No ha cargado planilla"
    fechaplanilla = "No ha cargado planilla"
    valortotalplanilla = "No ha cargado planilla"
    periodoplanilla = "No ha cargado planilla"
    nombresalud = "No ha cargado planilla"
    valorsalud = "No ha cargado planilla"
    nombrearl = "No ha cargado planilla"
    valorarl = "No ha cargado planilla"
    nombrepension = "No ha cargado planilla"
    valorpension = "No ha cargado planilla"
    lugar = "No ha cargado actividades"
    fechaact = "No ha cargado actividades"
    actividadess = "No ha cargado actividades"
    resultadoactividades = "No ha cargado actividades"
    estado = "Pendiente cargue de pdf"
    observacionesc = "Usuario no puede pasar cuenta"
    numeroacta = 0
    periodoap = "Usuario no ha cargado seguimiento de cuentas"
    numerocuentapago = 0
    cuentapago= "Usuario no ha cargado entidad bancaria"
    cedula = 0
    #######CUANDO EL USUARIO ESTA CREADO Y NO TIENE DOCUMENTOS NO CARGA
    if usuario.objects.filter(usuario=username).exists():
        nombre_usuario = usuario_obj.nombre
        segundo_nombre = usuario_obj.segundonombre #HASTA AQUI VA BIEN
        primer_apellido = usuario_obj.primerapellido
        segundo_apellido = usuario_obj.segundoapellido
        cedula = usuario_obj.cedula
        estado = "Pendiente cargue de pdf"
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
            estado = "Pendiente cargue del contrato"
        #else: 
            #VALIDAR CON CONDICIONAL CUANDO EL USUARIO NO TIENE DOCUMENTOS
            #return redirect('usuarios')
            ###########GESTION DE CONTRATACION RP########################  
            usuario_obj3 = rp.objects.filter(usuario_id=cedula).first()
            if rp.objects.filter(usuario_id=cedula).exists():
                numerorp = usuario_obj3.numero
                fecharp = usuario_obj3.fecha
                progreso=30
                estado = "Pendiente cargue de acta de inicio"
                ###########GESTION DE CONTRATACION ACTA INICIO########################  
                usuario_obj4 = actainicio.objects.filter(usuario_id=cedula).first()
                if actainicio.objects.filter(usuario_id=cedula).exists():
                    numeroai = usuario_obj4.numero
                    fechaai = usuario_obj4.fecha
                    progreso=40
                    estado = "Pendiente cargue de planilla"
                    ###########GESTION DE USUARIO PLANILLA########################  
                    usuario_obj5 = planilla.objects.filter(usuario_id=cedula).first()
                    if planilla.objects.filter(usuario_id=cedula).exists():
                        numeroplanilla = usuario_obj5.numero
                        fechaplanilla = usuario_obj5.fecha
                        valortotalplanilla = usuario_obj5.valortotal
                        periodoplanilla = usuario_obj5.periodo
                        nombresalud = usuario_obj5.nombresalud
                        valorsalud = usuario_obj5.valorsalud
                        nombrearl = usuario_obj5.nombrearl
                        valorarl = usuario_obj5.valorarl
                        nombrepension = usuario_obj5.nombrepension
                        valorpension = usuario_obj5.valorpension
                        progreso=50
                        estado = "Pendiente cargue de actividades"
                        usuario_obj6 = actividades.objects.filter(usuario_id=cedula).first()
                        if actividades.objects.filter(usuario_id=cedula).exists():
                            lugar = usuario_obj6.lugar
                            fechaact = usuario_obj6.fecha
                            actividadess = usuario_obj6.actividades
                            resultadoactividades = usuario_obj6.resultadoactvidades
                            progreso=60
                            estado = "Pendiente cargar acta de pago"
                            ##############ACTA DE PAGO############################
                            usuario_obj7 = actapago.objects.filter(usuario_id=cedula).first()
                            if actapago.objects.filter(usuario_id=cedula).exists():
                                 numeroacta = usuario_obj7.numeroacta
                                 periodoap = usuario_obj7.periodo
                                 progreso=80
                                 estado = "Pendiente cargar certificado de seguimiento de cuentas"
                                 usuario_obj8 = certificadoseguimiento.objects.filter(usuario_id=cedula).first()
                                 if certificadoseguimiento.objects.filter(usuario_id=cedula).exists():
                                    numerocuentapago = usuario_obj8.numerocuentapago
                                    cuentapago = usuario_obj8.cuentapago
                                    progreso=100
                                    estado = "Por pasar cuenta"
                                    observacionesc = "Pendiente enviar cuenta"
   
                     
    else:
        nombre_usuario = "No tiene nombre creado"
        segundo_nombre = ""
        primer_apellido = "No ha creado apellido"
        segundo_apellido = ""
        cedula = 0
        estado = "No ha cargado documentos"
        email = "No tiene email creado"
        supervisor = "No tiene supervisor asignado"
        numero = 0
        objeto = "No tiene contrato asignado"
        valor = "No tiene contrato asignado"
        fechaterminacion = "No tiene contrato asignado"
        duracion = "No tiene contrato asignado"
        numerorp = "No tiene registro presupuetal asignado"
        fecharp = "No tiene registro presupuetal asignado"
        numeroai = "No tiene acta de inicio asignado"
        fechaai = "No tiene acta de inicio asignado"
        progreso = 1
        #######################PLANILLA###############
        numeroplanilla = "No ha cargado planilla"
        fechaplanilla = "No ha cargado planilla"
        valortotalplanilla = "No ha cargado planilla"
        periodoplanilla = "No ha cargado planilla"
        nombresalud = "No ha cargado planilla"
        valorsalud = "No ha cargado planilla"
        nombrearl = "No ha cargado planilla"
        valorarl = "No ha cargado planilla"
        nombrepension = "No ha cargado planilla"
        valorpension = "No ha cargado planilla"
        ########ACTIVIDADES############################
        lugar = "No ha cargado actividades"
        fechaact = "No ha cargado actividades"
        actividadess = "No ha cargado actividades"
        resultadoactividades = "No ha cargado actividades"
        estado = "Pendiente cargue de documentos"
        observacionesc = "Usuario no tiene documentos pdf"
        numeroacta = 0
        periodoap = "Usuario no ha cargado seguimiento de cuentas"
        numerocuentapago = 0
        cuentapago= "Usuario no ha cargado entidad bancaria"
    return render(request, 'perfil.html', {'formper': formper, 'username': username, 'nombre_usuario': nombre_usuario, 'segundo_nombre': segundo_nombre, 'primer_apellido': primer_apellido, 'segundo_apellido': segundo_apellido, 'cedula': cedula, 'estado': estado, 'email': email,
                                        'supervisor': supervisor, 'numero': numero, 'objeto': objeto, 'valor': valor, 'fechaterminacion': fechaterminacion, 'duracion': duracion, 'numerorp': numerorp, 'fecharp': fecharp, 'numeroai': numeroai, 'progreso': progreso, 'fechaai': fechaai,
                                        'numeroplanilla': numeroplanilla, 'fechaplanilla': fechaplanilla, 'valortotalplanilla': valortotalplanilla, 'periodoplanilla': periodoplanilla, 'nombresalud': nombresalud, 'valorsalud': valorsalud, 'nombrearl': nombrearl, 'valorarl': valorarl,
                                        'nombrepension': nombrepension, 'valorpension': valorpension, 'lugar': lugar, 'fechaact': fechaact, 'actividadess': actividadess, 'resultadoactividades': resultadoactividades, 'observacionesc': observacionesc, 'numeroacta': numeroacta,
                                        'periodoap': periodoap, 'numerocuentapago': numerocuentapago, 'cuentapago': cuentapago})
#############TRAE DATOS SEGUN CORRESPONDE ###################
    
#gestion de documentos de usuarios
def documentos_usuario(request):
    form = Contratou(request.POST ,request.FILES)
    username = request.user.username
    cedula = 0
    numero = "No tiene contrato asignado"
    numeroproceso = "No tiene contrato asignado"
    objeto = "No tiene contrato asignado"
    fechaperfeccionamiento = "No tiene asignado"
    valor = "No tiene contrato asignado"
    fechaterminacion = "No tiene contrato asignado"
    duracion = "No tiene contrato asignado"
    estado = "Pendiente cargue de documentos"
    numerorp = "No tiene Registro presupuestal asignado"
    fecharp = "No tiene Registro presupuestal asignado"
    estadorp = "No tiene Registro presupuestal asignado"
    numeroai = "No tiene Acta de inicio asignado"
    fechaai = "No tiene Acta de inicio asignado"
    estadoai = "No tiene Acta de inicio asignado"
    numeroplanilla = "No tiene planilla asignado"
    fechaplanilla = "No tiene planilla asignado"
    estadoplanilla = "No tiene Acta de inicio asignado"
    lugar = "No tiene actividades asignado"
    fechaact = "No tiene actividades asignado"
    numeroacta = 1
    periodoap = "No tiene actividades asignado"
    numerocuentapago = "Numero de la entidad bancaria"
    cuentapago = "Nombre de la entidad bancaria"
    valorc = "No tiene asignado"
    fechacontrato = "No tiene asignado"
    periodoplanilla = "No tiene asignado"
    valortotalplanilla = "No tiene asignado"
    nombresalud = "No tiene asignado"
    nombrepension = "No tiene asignado"
    valorpension = "No tiene asignado"
    valorsalud = "No tiene asignado"
    nombrearl = "No tiene asignado"
    valorarl = "No tiene asignado"
    supervisor = ""
    lista = ['numero', 'numeroproceso', 'objeto', 'fechaperfeccionamiento', 'valor', 'fechacontrato', 'fechaterminacion', 'duracion','cedula']
    #primero me traigo los datos de usuario
    usuario_objr = usuario.objects.filter(usuario=username).first()
    if usuario.objects.filter(usuario=username).exists():
        cedula = usuario_objr.cedula
        supervisor = usuario_objr.supervisor
        usuario_objr2 = contrato.objects.filter(usuario_id=cedula).first()
        if contrato.objects.filter(usuario_id=cedula).exists():
            numero = usuario_objr2.numero
            numeroproceso = usuario_objr2.numeroproceso
            objeto = usuario_objr2.objeto
            fechaperfeccionamiento = usuario_objr2.fechaperfeccionamiento
            valorc = usuario_objr2.valor
            fechacontrato = usuario_objr2.fechacontrato
            fechaterminacion = usuario_objr2.fechaterminacion
            duracion = usuario_objr2.duracion
            estado = "Cargado"
            usuario_objr3 = rp.objects.filter(usuario_id=cedula).first()
            if rp.objects.filter(usuario_id=cedula).exists():
                numerorp = usuario_objr3.numero
                fecharp = usuario_objr3.fecha
                estadorp = "Cargado"
                usuario_objr4 = actainicio.objects.filter(usuario_id=cedula).first()
                if actainicio.objects.filter(usuario_id=cedula).exists():
                    numeroai = usuario_objr4.numero
                    fechaai = usuario_objr4.fecha
                    estadoai = "Cargado"
                    usuario_objr5 = planilla.objects.filter(usuario_id=cedula).first()
                    if planilla.objects.filter(usuario_id=cedula).exists():
                        numeroplanilla = usuario_objr5.numero
                        fechaplanilla = usuario_objr5.fecha
                        valortotalplanilla = usuario_objr5.valortotal
                        periodoplanilla = usuario_objr5.periodo
                        nombresalud = usuario_objr5.nombresalud
                        valorsalud = usuario_objr5.valorsalud
                        nombrearl = usuario_objr5.nombrearl
                        valorarl = usuario_objr5.valorarl
                        nombrepension = usuario_objr5.nombrepension
                        valorpension = usuario_objr5.valorpension
                        estadoplanilla = "Cargado"
                        usuario_objr6 = actividades.objects.filter(usuario_id=cedula).first()
                        if actividades.objects.filter(usuario_id=cedula).exists():
                            lugar = usuario_objr6.lugar
                            fechaact = usuario_objr6.fecha
                            usuario_objr7 = actapago.objects.filter(usuario_id=cedula).first()
                            if actapago.objects.filter(usuario_id=cedula).exists():
                                 numeroacta = usuario_objr7.numeroacta
                                 periodoap = usuario_objr7.periodo
                                 usuario_objr8 = certificadoseguimiento.objects.filter(usuario_id=cedula).first()
                                 if certificadoseguimiento.objects.filter(usuario_id=cedula).exists():
                                    numerocuentapago = usuario_objr8.numerocuentapago
                                    cuentapago = usuario_objr8.cuentapago
    else:
        cedular = 0
        numero = "No tiene contrato asignado"
        numeroproceso = "No tiene contrato asignado"
        objeto = "No tiene contrato asignado"
        valor = "No tiene contrato asignado"
        fechaterminacion = "No tiene contrato asignado"
        duracion = "No tiene contrato asignado"
        estado = "Pendiente cargue de documentos"
        numerorp = "No tiene Registro presupuestal asignado"
        fecharp = "No tiene Registro presupuestal asignado"
        estadorp = "No tiene Registro presupuestal asignado"
        numeroai = "No tiene Acta de inicio asignado"
        fechaai = "No tiene Acta de inicio asignado"
        estadoai = "No tiene Acta de inicio asignado"
        numeroplanilla = "No tiene planilla asignado"
        fechaplanilla = "No tiene planilla asignado"
        estadoplanilla = "No tiene Acta de inicio asignado"
        lugar = "No tiene actividades asignado"
        fechaact = "No tiene actividades asignado"
        numeroacta = 1
        periodoap = "No tiene actividades asignado"
        numerocuentapago = "Numero de la entidad bancaria"
        cuentapago = "Nombre de la entidad bancaria"
        fechaperfeccionamiento = "No tiene asignado"
        valorc = "No tiene asignado"
        fechacontrato = "No tiene asignado"
        periodoplanilla = "No tiene asignado"
        valortotalplanilla = "No tiene asignado"
        nombresalud = "No tiene asignado"
        nombrepension = "No tiene asignado"
        valorpension = "No tiene asignado"
        valorsalud = "No tiene asignado"
        nombrearl = "No tiene asignado"
        valorarl = "No tiene asignado"
        supervisor = "No tiene asignado"
    ### Registros de documentos##################
    if form.is_valid():
        form.save()
        messages.success(request, 'Documento guardado')
        #### AQUI IRA LA PARTE DEL ANALISIS DE DOCUMENTO ####
        #### AQUI IRA LA PARTE DEL ANALISIS DE DOCUMENTO ####
        return render(request, 'sdocumentos_usuario.html')
    formrp = Rp(request.POST or None)
    if formrp.is_valid():
        formrp.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos_usuario.html')
    forminicio = Actainicio(request.POST or None)
    if forminicio.is_valid():
        forminicio.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos_usuario.html')
    formplanilla = Planilla(request.POST or None)
    if formplanilla.is_valid():
        formplanilla.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos_usuario.html')
    formactividades = Actividades(request.POST or None)
    if formactividades.is_valid():
        formactividades.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos_usuario.html')
    formactapago = Actapago(request.POST or None)
    if formactapago.is_valid():
        formactapago.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos_usuario.html')
    formcertificadoseguimiento = Certificadoseguimiento(request.POST or None)
    if formcertificadoseguimiento.is_valid():
        formcertificadoseguimiento.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'sdocumentos_usuario.html')
    return render(request, 'sdocumentos_usuario.html', {'form': form, 'formrp': formrp, 'forminicio': forminicio, 'formplanilla': formplanilla, 'formactividades': formactividades, 'formactapago': formactapago, 'formcertificadoseguimiento': formcertificadoseguimiento, 'username': username,
                                                        'numero': numero, 'duracion': duracion, 'estado': estado, 'cedula': cedula, 'numeroproceso': numeroproceso, 'numerorp': numerorp, 'fecharp': fecharp, 'estadorp': estadorp,'numeroai': numeroai, 'fechaai': fechaai, 'estadoai': estadoai,
                                                        'numeroplanilla': numeroplanilla, 'fechaplanilla': fechaplanilla, 'estadoplanilla': estadoplanilla, 'lugar': lugar, 'fechaact': fechaact, 'numeroacta': numeroacta, 'periodoap': periodoap, 'numerocuentapago': numerocuentapago,
                                                        'cuentapago': cuentapago, 'lista': lista, 'objeto': objeto, 'fechaperfeccionamiento': fechaperfeccionamiento, 'valorc': valorc, 'fechacontrato': fechacontrato, 'fechaterminacion': fechaterminacion, 'periodoplanilla': periodoplanilla,
                                                        'valortotalplanilla': valortotalplanilla, 'nombresalud': nombresalud, 'nombrepension': nombrepension, 'valorpension': valorpension, 'valorsalud': valorsalud, 'nombrearl': nombrearl, 'valorarl': valorarl, 'supervisor': supervisor})
#gestion de documentos de usuarios

def list_usuarios(request):
    usuarios = list(usuario.objects.values())
    data = {'usuarios': usuarios}
    return JsonResponse(data)


def usuarios_pendientes(request):
    return render(request, 'usuariospendientes.html')

#opcion de eliminar aqui
def eliminar(request, cedula):
    us = usolicitudes.objects.get(cedula=cedula)
    us.delete()
    return redirect('usuario_pendient')
#opcion de eliminar aqui   

#primero guardar la solicitud en usuarios registrados
##segundo asignarle valores al usuario registrado
#tercero eliminarlo la solicitud
def guardar(request):
    formpers = InsertFormU(request.POST or None)
    if formpers.is_valid():
        formpers.save()
        return redirect('usuario_pendient')
    return render(request, 'usuariospendient.html', {'formpers': formpers})
    
    
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
    return redirect('login')

#USUARIOS PENDIENTES SIN DATATABLE
def usuario_pendiente(request):
    #usuario = {
        #'nombre': '',
        #'segundonombre': '',
        #'primerapellido': '',
        #'segundoapellido': '',
        #'cargo': '',
        #'email': '',
        #'supervisor': '',
        #'tipodocumento': '',
        #'cedula': '',
        #'rol': ''
    #}
    return render(request, 'usuariopendiente.html')


def obtenercedula(request, cedula):
    usuarios = get_object_or_404(usolicitudes, cedula=cedula)
    data = {
        'nombre': usuarios.nombre,
        'segundonombre': usuarios.segundonombre,
        'primerapellido': usuarios.primerapellido,
        'segundoapellido': usuarios.segundoapellido,
        'cedula': usuarios.cedula,
        'cargo': usuarios.cargo,
        'email': usuarios.email,
        'supervisor': usuarios.supervisor,
        'tipo_documento': usuarios.tipo_documento,
        'rol': usuarios.rol,
    }
    return JsonResponse(data)


def eliminarregistro(request, cedula):
    if request.method == 'DELETE':
        usuario = get_object_or_404(usolicitudes, cedula=cedula)
        usuario.delete()
        return JsonResponse({'mensaje': 'Registro eliminado correctamente.'}, status=200)
    else:
        return HttpResponseNotAllowed(['DELETE'])
    
#usuarios pendientes opcion de guardado    
def usuarios_pendient(request):
    datos = usolicitudes.objects.values()
    forupendiente = InsertFormU(request.POST or None)
    foruelimina = Users(request.POST or None)
    
    if forupendiente.is_valid():
        forupendiente.save()
        messages.success(request, 'Usuario agregado')
        username = forupendiente.cleaned_data.get('usuario')
        email = forupendiente.cleaned_data.get('email')
        password = forupendiente.cleaned_data.get('contrasena')
        new_user = User.objects.create_user(username=username, email=email, password=password) 
        new_user.save()
        user = authenticate(username=username, password=password)     
       
    elif foruelimina.is_valid():
        cedula = foruelimina.cleaned_data.get('cedula')
        cuenta = usolicitudes.objects.filter(cedula=cedula)
        cuenta.delete()
        return redirect('usuario_pendient')
    return render(request, 'usuariospendient.html', {'datos': datos, 'forupendiente': forupendiente, 'foruelimina': 'foruelimina'})

def eliminador(request, cedula):
    usuario = usolicitudes.objects.get(cedula=cedula)
    form_elimina = Users(request.POST or None, instance=usuario)
    if request.method == 'POST' and form_elimina.is_valid():
        usuario.delete()
        return redirect('usuario_pendiente')
    return render(request, 'eliminar_usuario.html', {'form_elimina': form_elimina, 'usuario': usuario})

#############CAMBIOS NUEVOS ##################
def ops(request):
    username = request.user.username
    return render(request, 'ops.html', {'username': username})

def cuentas(request):
    username = request.user.username
    return render(request, 'cuentas.html', {'username': username})