from django.contrib import admin
from .models import  cuentatesoreriacontratista

class cuentatesoreriaContratista(admin.ModelAdmin):
    list_display=('nombrecompleto', 'objetocontrato', 'ordenpago','egreso')
    search_fields = ('nombrecompleto',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(cuentatesoreriacontratista, cuentatesoreriaContratista)


