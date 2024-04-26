from django.http import HttpResponse
from django.template import Template,Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render #para llamar otra plantilla


def saludo(request):
    
    return HttpResponse("INICALIZACION DEL PROYECTO DESDE GESTION DE CUENTAS"); #lo hacemos con httreponse

def despedida(request):
    
    return HttpResponse("FINALIZACION DEL PROYECTO");


def calculaEdad(request, agno):
    #ejemplo pasando parametros
    edadActual = 27
    periodo=agno-2023
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)
    
    return HttpResponse(documento)

#def saludo2(request):
   
#    return render(request, 'index.html')

def saludo3(request):
    #ESTE EJEMPLO ES PARA ABIR UNA PLANTILLA CON SOLO CODIGO HTML
    doc_externo=open("C:/xampp/htdocs/sistemas_cuentas/sistemas_cuentas/templates/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

##EJEMPLO CON LA PARTE MODELO
class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def plantillas(request):
    #EJEMPLO DE PLANTILLA PASANDOLE VARIABLES ESTATICAS
    fecha_Actual=datetime.datetime.now()
    nombre="Danny"
    ##otra forma
    p1=Persona("Stiveens", "Gil")#AQUI OBTIENE DEL MODELO PERSONA
    
    doc_externo=open("C:/xampp/htdocs/sistemas_cuentas/sistemas_cuentas/templates/plantilla2.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    #AQUI ESTAN LAS DOS FORMAS
    ctx=Context({"nombre_persona": p1.nombre, "hora_Actual": fecha_Actual})
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

#def home(request):
#    return render(request, 'sistemas_cuentas/home.html')
#def incrustada(request):
#     return render(request, "C:/xampp/htdocs/sistemas_cuentas/sistemas_cuentas/templates/plantilla2.html")
 
def index(request):
    return render(request, 'C:/xampp/htdocs/sistemas_cuentas/sistemas_cuentas/templates/index.html')



