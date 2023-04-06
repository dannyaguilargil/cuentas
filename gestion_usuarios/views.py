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
from gestion_usuarios.forms import User
from django.contrib import messages

#def  usuarios(request):
#     return render(request, 'C:/xampp/htdocs/sistemas_cuentas/gestion_usuarios/templates/index.html')

def  usuarios(request):
     return render(request, 'usuarios.html') # se modifica esto con lo anterior pero para no poner toda la ruta, cambiando en settin.py insatllerds app poniendo la ruta

def home(request):
    return render(request, 'home.html')

def solicitud_usuario(request):
    #Aqui va el formulario dinamico
    formulario = User(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, f'¡Cuenta creada!')
        return render(request, 'solicitud.html')
    return render(request, 'solicitud.html', {'formulario': formulario})

def crear(request):
    return render(request, 'crear.html')

def documentos(request):
    return render(request, 'sdocumentos.html')

def perfil(request):
    return render(request, 'perfil.html')

def documentos_usuario(request):
    return render(request, 'sdocumentos_usuario.html')

def list_usuarios(request):
    usuarios = list(usuario.objects.values())
    data = {'usuarios': usuarios}
    return JsonResponse(data)

def usuarios_pendientes(request):
    return render(request, 'usuariospendientes.html')

def usolicitud(request):
    usuarios = list(usolicitudes.objects.values())
    data = {'usuarios': usuarios}
    return JsonResponse(data)

#def incrustada(request):
#     return render(request, "C:/xampp/htdocs/sistemas_cuentas/sistemas_cuentas/templates/plantilla2.html")
 



