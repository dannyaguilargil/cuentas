
from django.shortcuts import render
from gestion_supervisor.models import cuentasupervisor


def  presupuesto(request):
     datos = cuentasupervisor.objects.values()
     return render(request, 'presupuesto.html', { 'datos': datos }) 



