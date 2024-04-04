from django.shortcuts import render,redirect
from django.contrib import messages
########################################
from django.http.response import JsonResponse
from django.http import JsonResponse
from gestion_usuarios.models import usolicitudes,usuario
from gestion_identidades.forms import Formidentidades
from gestion_identidades.models import solicitudsistema

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
            messages.success(request, 'La solicitud se ha guardado exitosamente.')
            return redirect('identidades')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, revise los datos ingresados.')

    else:
        formularios = Formidentidades()

     ####para realizar la inserccion del formato de identidades ####
    return render(request, 'identidades.html' , {'username': username, 'formularios': formularios})

def pazysalvo(request):
    return render(request, 'pazysalvo.html')

##aqui debe ir como traigo ese dato en json ""
def usolicitud(request):
    usuarios = list(solicitudsistema.objects.values())
    data = {'solicitud': usuarios}
    return JsonResponse(data)
## aqui debe ir como traigo los sistemas pendientes en json ###

def identidadespendientes(request):
    #solicitud_obj = ""
    datos = solicitudsistema.objects.values()
    return render(request, 'pendientes.html', {'datos': datos})

def identidadespendientesadmin(request):
    #solicitud_obj = ""
    datos = solicitudsistema.objects.values()
    return render(request, 'pendientesadmin.html', {'datos': datos})
