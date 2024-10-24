from django.contrib import admin
from .models import  solicitudsistema,pazysalvo,solicitudsistemasupervisor,aplicativo,modulo,solicitudsistemaadmin,solicitudsistemarechazado,solicitudsistemarechazadoadm,pazysalvoaprobado,pazysalvorechazado

class solicitudSistema(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'aplicativo', 'modulo', 'tiposolicitud', 'fecha_actualizacion')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(solicitudsistema, solicitudSistema)

class solicitudSistemasupervisor(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'aplicativo', 'modulo', 'tiposolicitud', 'observacionessup')
    search_fields = ('id',)
admin.site.register(solicitudsistemasupervisor, solicitudSistemasupervisor)

class solicitudSistemaAdmin(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'aplicativo', 'tiposolicitud', 'observaciones')
    search_fields = ('id',)
admin.site.register(solicitudsistemaadmin, solicitudSistemaAdmin)

class pazySalvo(admin.ModelAdmin):
    list_display=('id', 'usuario', 'permisos','rfid','fecha_creacion','fecha_actualizacion')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(pazysalvo, pazySalvo)

class Aplicativo(admin.ModelAdmin):
    list_display=('id', 'nombre', 'activo', 'fecha_creacion','fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(aplicativo, Aplicativo)

class Modulo(admin.ModelAdmin):
    list_display=('id', 'aplicativo', 'nombre', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(modulo, Modulo)

class solicitudSistemaRechazado(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'aplicativo', 'modulo', 'observacionessup', 'fecha_actualizacion')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(solicitudsistemarechazado, solicitudSistemaRechazado)

class solicitudRechazadoAdm(admin.ModelAdmin):
    list_display=('id', 'nombre', 'primerapellido','cedula', 'aplicativo', 'modulo', 'observacionesadm', 'fecha_actualizacion')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(solicitudsistemarechazadoadm, solicitudRechazadoAdm)

class pazySalvoaprobado(admin.ModelAdmin):
    list_display=('id', 'usuario', 'permisos','rfid','fecha_creacion','fecha_actualizacion')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(pazysalvoaprobado, pazySalvoaprobado)

class pazysalvoRechazado(admin.ModelAdmin):
    list_display=('id', 'usuario', 'permisos','rfid','fecha_creacion','fecha_actualizacion')
    search_fields = ('id',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(pazysalvorechazado, pazysalvoRechazado)