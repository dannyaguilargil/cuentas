from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from gestion_supervisor.models import cuentasupervisor, cuentasupervisorcontratista
from gestion_presupuesto.forms import InsertFormp
from django.contrib import messages
from gestion_supervisor.models import cuentasupervisorcontratista

@login_required
def  presupuesto(request):
     datos = cuentasupervisorcontratista.objects.values()
     formpresu = InsertFormp(request.POST, request.FILES)
     if formpresu.is_valid():
        formpresu.save()
        cedula = request.POST['cedula']
        ###eliminar la cuenta una vez registrado
        cs = cuentasupervisorcontratista.objects.get(cedula=cedula)
        cs.delete()
        messages.success(request, 'Cuenta registrada por presupuesto') #falta la gestion del mensaje
        return redirect('presupuesto')
     return render(request, 'presupuesto.html', { 'datos': datos, 'formpresu': formpresu }) 



