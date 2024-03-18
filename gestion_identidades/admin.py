from django.contrib import admin
from .models import  solicitudsistema

class solicitudSistema(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(solicitudsistema, solicitudSistema)
