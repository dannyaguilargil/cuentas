from django.contrib import admin
from .models import  solicitudsistema,pazysalvo,solicitudsistemasupervisor,aplicativo,modulo

class solicitudSistema(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'apicativo', 'tiposolicitud', 'observaciones')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(solicitudsistema, solicitudSistema)


class solicitudSistemasupervisor(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'apicativo', 'tiposolicitud', 'observaciones')
    search_fields = ('id',)
admin.site.register(solicitudsistemasupervisor, solicitudSistemasupervisor)

class pazySalvo(admin.ModelAdmin):
    list_display=('id', 'cedula', 'permisos','rfid')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(pazysalvo, pazySalvo)

class Aplicativo(admin.ModelAdmin):
    list_display=('id', 'nombre', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(aplicativo, Aplicativo)

class Modulo(admin.ModelAdmin):
    list_display=('id', 'aplicativo', 'nombre', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(modulo, Modulo)