from django.contrib import admin
from .models import  entecontrol,dependencia,informe,alarma,entrega,evidencia
from django.utils.html import format_html

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

    def display_normativa(self, obj):
        if obj.normativa:
            file_url = obj.normativa.url
            file_url = file_url.replace('/sistemas_cuentas/', '/')
            #file_url = reverse('sistemas_cuentas:archivo', args=[obj.numero])
            return format_html('<a href="{}" target="_blank" style="color: grey;">Ver normativa</a>', file_url)
        else:
            return '-'
    display_normativa.short_description = 'Normativa'

    list_display= ('id', 'nombre', 'display_normativa', 'entecontrol', 'dependencia', 'fecha_actualizacion')
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

    def display_evidencia(self, obj):
        if obj.archivo:
            file_url = obj.archivo.url
            file_url = file_url.replace('/sistemas_cuentas/', '/')
            #file_url = reverse('sistemas_cuentas:archivo', args=[obj.numero])
            return format_html('<a href="{}" target="_blank" style="color: grey;">Ver evidencia</a>', file_url)
        else:
            return '-'
    display_evidencia.short_description = 'Archivo'
    list_display= ('id', 'entrega', 'nombre', 'fecha_actualizacion', 'display_evidencia')
admin.site.register(evidencia, Evidencia)