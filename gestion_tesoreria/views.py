
from django.shortcuts import render
from gestion_presupuesto.models import cuentapresupuesto

def  tesoreria(request):
     datos = cuentapresupuesto.objects.values()
     return render(request, 'tesoreria.html', { 'datos': datos }) # se modifica esto con lo anterior pero para no poner toda la ruta, cambiando en settin.py insatllerds app poniendo la ruta



