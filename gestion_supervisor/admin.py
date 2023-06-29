from django.contrib import admin
from .models import  cuentasupervisor, cuentasupervisorcontratista

#admin.site.register(cuentasupervisor)

####### GESTION DE LA CUENTA CONTRATISTA
class cuentasupervisorContratista(admin.ModelAdmin):
    list_display=('nombrecompleto', 'objetocontrato', 'pdfplanilla')
    search_fields = ('nombre',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(cuentasupervisorcontratista, cuentasupervisorContratista)