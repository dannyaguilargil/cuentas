from django.contrib import admin
from .models import  solicitudsistema,pazysalvo

class solicitudSistema(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'apicativo', 'tiposolicitud', 'observaciones')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(solicitudsistema, solicitudSistema)


class pazySalvo(admin.ModelAdmin):
    list_display=('id', 'cedula', 'permisos','rfid')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(pazysalvo, pazySalvo)