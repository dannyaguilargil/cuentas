from django.contrib import admin
from .models import  entecontrol,dependencia,informe,alarma,entrega,evidencia
# Register your models here.
class enteControl(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'descripcion', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(entecontrol, enteControl)

class Dependencia(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'responsable', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(dependencia, Dependencia)

###informes ###
class Informe(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'normativa', 'fecha_actualizacion', 'fechaentregapendiente')
    search_fields = ('nombre',)
admin.site.register(informe, Informe)

class Alarma(admin.ModelAdmin):
    list_display= ('id', 'informe', 'activo', 'dias', 'fecha_actualizacion')
    search_fields = ('informe',)
admin.site.register(alarma, Alarma)

class Entrega(admin.ModelAdmin):
    list_display= ('id', 'informe', 'fecha', 'activo', 'fecha_actualizacion')
    search_fields = ('informe',)
admin.site.register(entrega, Entrega)

class Evidencia(admin.ModelAdmin):
    list_display= ('id', 'entrega', 'nombre', 'activo', 'fecha_actualizacion')
    search_fields = ('nombre',)
admin.site.register(evidencia, Evidencia)