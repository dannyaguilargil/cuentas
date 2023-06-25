
from django.shortcuts import render
from gestion_usuarios.models import usolicitudes,cuentausuario, cuentacontratista
from gestion_usuarios.forms import Users

def  supervisor(request):
     username = request.user.username
     datos = cuentacontratista.objects.values()
     return render(request, 'supervisor.html', {'datos': datos }) 



