from django.contrib import admin
from .models import  cuentasupervisor, cuentasupervisorcontratista,supervisor

#admin.site.register(cuentasupervisor)

####### GESTION DE LA CUENTA CONTRATISTA
#class cuentasupervisorContratista(admin.ModelAdmin):
#    list_display=('nombrecompleto', 'objetocontrato', 'pdfplanilla')
#    search_fields = ('nombre',)#cuadrito de busqueda dentro del panel de administracion
#admin.site.register(cuentasupervisorcontratista, cuentasupervisorContratista)

class supervisores(admin.ModelAdmin):
    list_display=('nombrecompleto', 'cedula', 'cargo')
    search_fields = ('nombrecompleto',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(supervisor, supervisores)