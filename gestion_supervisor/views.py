
from django.shortcuts import render
from gestion_usuarios.models import usolicitudes,cuentausuario, cuentacontratista,usuario,contrato,planilla,rp,cuentabancaria
from gestion_usuarios.forms import Users
from django.http import HttpResponse
from xhtml2pdf import pisa
from datetime import datetime
import calendar
import locale, inflect

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


def seguimientohtml(request):
    nombre = ""
    return render(request, 'seguimiento.html', {'nombre': nombre})
    
    #SELECT count(*) from gestion_usuarios_contrato where usuario_id=1090492324;
    
def seguimiento(request,cedula):
    nombre = "" #Lo remplazo con el que traiga del modelo
    segundonombre = ""
    primerapellido = ""
    segundoapellidos = ""
    numerocontratos = ""
    numeroproceso = ""
    aux = cedula
    supervisor = ""
    objetocontrato = ""
    fechaperfeccionamientos = ""
    duracion = ""
    dependenciausuario = ""
    duracioncontrato = ""
    numerorp = ""
    fechacontrato = ""
    fechaterminacion = ""
    valorpagar = 1
    numeroplanilla = ""
    nombresalud = ""
    valorsalud = ""
    nombrepension = ""
    valorpension = ""
    nombrearl = ""
    valorarl = ""
    numerocuentabancaria = ""
    tipocuenta = ""
    nombrecb = ""
    nombre_mes = ""
    dia = ""
    año = ""
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
            usuario_obj3 = rp.objects.filter(usuario_id=cedula).first()
            if rp.objects.filter(usuario_id=cedula).exists():
                  numerorp = usuario_obj3.numero
                  usuario_obj4 = planilla.objects.filter(usuario_id=cedula).first()
                  if planilla.objects.filter(usuario_id=cedula).exists():
                      numeroplanilla = usuario_obj4.numero
                      nombresalud = usuario_obj4.nombresalud
                      valorsalud = usuario_obj4.valorsalud
                      nombrepension = usuario_obj4.nombrepension
                      valorpension = usuario_obj4.valorpension
                      nombrearl = usuario_obj4.nombrearl
                      valorarl = usuario_obj4.valorarl
                      usuario_obj5 = cuentabancaria.objects.filter(usuario_id=cedula).first()
                      if cuentabancaria.objects.filter(usuario_id=cedula).exists():
                          numerocuentabancaria = usuario_obj5.numero
                          tipocuenta = usuario_obj5.tipocuenta
                          nombrecb = usuario_obj5.nombrecb
                          fecha_actual = datetime.now()
                          locale.setlocale(locale.LC_TIME, 'es_ES')
                          nombre_mes = fecha_actual.strftime('%B')
                          #mes = fecha_actual.month
                          dia = fecha_actual.day
                          año = fecha_actual.year
                          # Establecer el idioma en español
                      
                      
    context = {'nombre': nombre, 'segundonombre': segundonombre, 'numerocontratos': numerocontratos, 'primerapellido': primerapellido, 'segundoapellidos': segundoapellidos, 'aux': aux,
               'objetocontrato': objetocontrato, 'numerorp': numerorp, 'fechacontrato': fechacontrato, 'fechaterminacion': fechaterminacion, 'supervisor': supervisor, 'numeroplanilla': numeroplanilla,
               'nombresalud': nombresalud, 'valorsalud': valorsalud, 'nombrepension': nombrepension, 'valorpension': valorpension, 'nombrearl': nombrearl, 'valorarl': valorarl, 'numerocuentabancaria': numerocuentabancaria,
               'tipocuenta': tipocuenta, 'nombrecb': nombrecb, 'nombre_mes': nombre_mes, 'dia': dia, 'año': año}
    template = render(request, 'seguimiento.html', context)
    
    # Crear un objeto HttpResponse con tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="seguimiento.pdf"'
    
    # Convertir la plantilla XHTML a PDF
    pisa_status = pisa.CreatePDF(template.content, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Ocurrió un error al generar el PDF')
    return response


