#from django.http import HttpResponse
#from django.template import Template,Context
#from django.template.loader import get_template
#from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
#para el uso de datatables
from django.http.response import JsonResponse
from gestion_usuarios.models import usuario
from gestion_usuarios.models import usolicitudes
from gestion_usuarios.models import prueba
from gestion_usuarios.models import contrato
from gestion_usuarios.forms import User
from gestion_usuarios.forms import Usuario
from gestion_usuarios.forms import Contrato, Rp, Actainicio, Planilla, Actividades, Actapago, Certificadoseguimiento
from django.contrib import messages

#def  usuarios(request):
#     return render(request, 'C:/xampp/htdocs/sistemas_cuentas/gestion_usuarios/templates/index.html')

def  base(request):
     return render(request, 'base_layout_usuarios.html') #archivo base de usuarios

def  usuarios(request):
     return render(request, 'usuarios.html') # se modifica esto con lo anterior pero para no poner toda la ruta, cambiando en settin.py insatllerds app poniendo la ruta

def home(request):
    return render(request, 'home.html')

#Aqui hago insercciones
def solicitud_usuario(request):
    #Aqui va el formulario dinamico
    formulario = User(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, f' Cuenta creada')
        return render(request, 'solicitud.html')
    return render(request, 'solicitud.html', {'formulario': formulario})
#aqui hago insecciones

def crear(request):
    formularios = Usuario(request.POST or None)
    if formularios.is_valid():
        formularios.save()
        messages.success(request, 'Cuenta creada')
        return render(request, 'crear.html')
    return render(request, 'crear.html',  {'formularios': formularios})

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

def perfil(request):
    return render(request, 'perfil.html')

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

#opcion de registro puro#
#def registro(request):
#    if request.method == 'POST':
#        numero = request.POST['numero']
#        numeroproceso = request.POST['numeroproceso']
#        objeto = request.POST['objeto']
#        fechaperfeccionamiento = request.POST['fechaperfeccionamiento']
#        valor = request.POST['valor']
#        fechacontrato = request.POST['fechacontrato']
#        fechaterminacion = request.POST['fechaterminacion']
#        duracion = request.POST['duracion']
#        registro = contrato(numero=numero, numeroproceso=numeroproceso, objeto=objeto, fechaperfeccionamiento=fechaperfeccionamiento, valor=valor, fechacontrato=fechacontrato, fechaterminacion=fechaterminacion, duracion=duracion)
#        registro.save()
#        return render(request, 'sdocumentos.html')

#opcion de registro puro#