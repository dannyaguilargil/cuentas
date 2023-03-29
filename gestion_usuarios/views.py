#from django.http import HttpResponse
#from django.template import Template,Context
#from django.template.loader import get_template
#from django.shortcuts import get_object_or_404
from django.shortcuts import render


#def  usuarios(request):
#     return render(request, 'C:/xampp/htdocs/sistemas_cuentas/gestion_usuarios/templates/index.html')

def  usuarios(request):
     return render(request, 'index.html') # se modifica esto con lo anterior pero para no poner toda la ruta, cambiando en settin.py insatllerds app poniendo la ruta

def home(request):
    return render(request, 'home.html')

def solicitud_usuario(request):
    return render(request, 'solicitud.html')

def crear(request):
    return render(request, 'crear.html')

def documentos(request):
    return render(request, 'sdocumentos.html')

def perfil(request):
    return render(request, 'perfil.html')

def documentos_usuario(request):
    return render(request, 'sdocumentos_usuario.html')





#def incrustada(request):
#     return render(request, "C:/xampp/htdocs/sistemas_cuentas/sistemas_cuentas/templates/plantilla2.html")
 



