
from django.shortcuts import render
from gestion_usuarios.models import usolicitudes,cuentausuario, cuentacontratista,usuario,contrato
from gestion_usuarios.forms import Users
from django.http import HttpResponse
from xhtml2pdf import pisa

def  supervisor(request):
     username = request.user.username
     cedula = 0
     datos = cuentacontratista.objects.values()
     return render(request, 'supervisor.html', {'datos': datos, 'cedula': cedula }) 

def pruebapdf(request, cedula):
    nombre = "" #Lo remplazo con el que traiga del modelo
    segundonombre = ""
    primerapellido = ""
    segundoapellidos = ""
    numerocontratos = ""
    numeroproceso = ""
    supervisor = ""
    objetocontrato = ""
    fechaperfeccionamientos = ""
    duracion = ""
    dependenciausuario = ""
    duracioncontrato = ""
    valorpagar = 1
    cuenta = 1 #remplazar por el numero de cuenta recibida
    ##############EXTRACCION DE DATOS APARTIR DE LA CEDULA############
    usuario_obj = usuario.objects.filter(cedula=cedula).first()
    if usuario.objects.filter(cedula=cedula).exists():
         nombre = usuario_obj.nombre
         segundonombre = usuario_obj.segundonombre
         primerapellido = usuario_obj.primerapellido
         segundoapellidos = usuario_obj.segundoapellido
         dependenciausuario = usuario_obj.dependencia
         usuario_obj2 = contrato.objects.filter(usuario_id=cedula).first()
         if contrato.objects.filter(usuario_id=cedula).exists():
            numerocontratos = usuario_obj2.numero
            numeroproceso = usuario_obj2.numeroproceso
            fechaperfeccionamientos = usuario_obj2.fechaperfeccionamiento
            fechacontrato = usuario_obj2.fechacontrato
            supervisor = usuario_obj2.supervisor
            archivo = usuario_obj2.archivo
            #archivo2 = archivo.replace('contratista', 'static')
            objetocontrato = usuario_obj2.objeto
            valorcontrato = usuario_obj2.valor
            fechaterminacion = usuario_obj2.fechaterminacion
            duracioncontrato = usuario_obj2.duracion
            cuenta = 1
            #valorpagar=valorcontrato/duracioncontrato 
            #########para valor a pagar es aux=valor/duracion
    ##############EXTRACCION DE DATOS APARTIR DE LA CEDULA############
    
    context = {'nombre': nombre, 'segundonombre': segundonombre, 'cedula': cedula, 'primerapellido': primerapellido, 'objetocontrato': objetocontrato, 'numerocontratos': numerocontratos, 'segundoapellidos': segundoapellidos,
               'fechaperfeccionamientos': fechaperfeccionamientos,'cuenta': cuenta,'duracion': duracion,'dependenciausuario': dependenciausuario, 'valorpagar': valorpagar, 'supervisor': supervisor}
    template = render(request, 'actapago.html', context)
    
    # Crear un objeto HttpResponse con tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="actapago.pdf"'
    
    # Convertir la plantilla XHTML a PDF
    pisa_status = pisa.CreatePDF(template.content, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Ocurrió un error al generar el PDF')
    return response

def pruebapdfactapago(request):
    nombre = ""
    return render(request, 'actapago.html', {'nombre': nombre})


