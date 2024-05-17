from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from gestion_presupuesto.models import cuentapresupuestocontratista
from django.contrib import messages
from gestion_tesoreria.forms import InsertFormt

@login_required
def  tesoreria(request):
     datos = cuentapresupuestocontratista.objects.values()
     formteso = InsertFormt(request.POST, request.FILES)
     if formteso.is_valid():
        formteso.save()
        cedula = request.POST['cedula']
        ###eliminar la cuenta una vez registrado
        cs = cuentapresupuestocontratista.objects.get(cedula=cedula)
        cs.delete()
        messages.success(request, 'Cuenta pagada por tesoreria') #falta la gestion del mensaje
        return redirect('tesoreria')
     return render(request, 'tesoreria.html', { 'datos': datos, 'formteso': formteso }) # se modifica esto con lo anterior pero para no poner toda la ruta, cambiando en settin.py insatllerds app poniendo la ruta



