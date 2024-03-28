from django.contrib import admin
from .models import  entecontrol,dependencia
# Register your models here.
class enteControl(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'descripcion', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(entecontrol, enteControl)

class Dependencia(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'responsable', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(dependencia, Dependencia)