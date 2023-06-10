
from django.shortcuts import render
from gestion_usuarios.models import usolicitudes,cuentausuario
from gestion_usuarios.forms import Users

def  supervisor(request):
     username = request.user.username
     datos = cuentausuario.objects.values()
     return render(request, 'supervisor.html', {'datos': datos }) 



