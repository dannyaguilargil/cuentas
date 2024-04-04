from django.contrib import admin
from .models import  usuario, usolicitudes, contrato, rp, actainicio, prueba, planilla, actividades, actapago, certificadoseguimiento, cuentausuario, cuentabancaria, cuentacontratista
#from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import os
from django.conf import settings
#Modificaciones del frontend
admin.site.site_header = "Administracion sistema de cuentas"
admin.site.site_title = "Administracion"
admin.site.index_title = "Bienvenido Administrador!"
#Modificaciones del frontend

# Listar por tabla a solicitudes de usuarios
class Usolicitud(admin.ModelAdmin):
    list_display=('nombre', 'primerapellido', 'segundoapellido', 'cedula', 'cargo')
    search_fields = ('nombre',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(usolicitudes, Usolicitud)
#Listar por tabla a solicitudes de usuarios

#listar por tablas usuarios
class User(admin.ModelAdmin):
    list_display= ('nombre', 'primerapellido', 'segundoapellido', 'cedula', 'rol')
    search_fields = ('nombre',)#cuadrito de busqueda dentro del panel de administracion
admin.site.register(usuario, User)
# listar por tablas usuarios

#listar por tabla los contrato en el panel de administracion
class Cont(admin.ModelAdmin):
    #aqui debe ir el nombre de la persona que pertenece el contrato
    list_display=('numero', 'objeto', 'valor', 'duracion','usuario_id','archivo')
    search_fields = ('numero',)#hace busqueda por numeros
    
    
    def display_archivo(self, obj):
        if obj.archivo:
            file_url = obj.archivo.url
            file_url = file_url.replace('/sistemas_cuentas/', '/')
            #file_url = reverse('sistemas_cuentas:archivo', args=[obj.numero])
            return format_html('<a href="{}" target="_blank" style="color: #E74C3C;">Ver pdf</a>', file_url)
        else:
            return '-'
    display_archivo.short_description = 'Archivo'

    list_display = ['numero', 'objeto', 'valor', 'fechacontrato', 'duracion', 'display_archivo']

admin.site.register(contrato, Cont)

#listar por tabla los contrato en el panel de administracion

#listar por tablas usuarios
class Rps(admin.ModelAdmin):
    list_display= ('numero', 'fecha', 'duracion', 'valor','usuario_id')
    search_fields = ('numero',)
    
    def display_archivo(self, obj):
        if obj.archivo:
            file_url = obj.archivo.url
            file_url = file_url.replace('/sistemas_cuentas/', '/')
            #file_url = reverse('sistemas_cuentas:archivo', args=[obj.numero])
            return format_html('<a href="{}" target="_blank" style="color: #E74C3C;">Ver pdf</a>', file_url)
        else:
            return '-'
    display_archivo.short_description = 'Archivo'
    
    list_display = ['numero', 'fecha', 'duracion', 'valor', 'usuario_id', 'display_archivo']
    
admin.site.register(rp, Rps)
#listar por tablas usuarios

#listar por tabla las acta de inicio en el panel de administracion
class Actainicio(admin.ModelAdmin):
    #aqui va el nombe o cedula de la persona que pasa el acta de inicio
    list_display=('numero','fecha','duracion', 'valor','usuario_id')
    search_fields = ('numero',)
    
    def display_archivo(self, obj):
        if obj.archivo:
            file_url = obj.archivo.url
            file_url = file_url.replace('/sistemas_cuentas/', '/')
            #file_url = reverse('sistemas_cuentas:archivo', args=[obj.numero])
            return format_html('<a href="{}" target="_blank" style="color: #E74C3C;">Ver pdf</a>', file_url)
        else:
            return '-'
    display_archivo.short_description = 'Archivo'
    
    list_display = ['numero', 'fecha', 'duracion', 'valor', 'usuario_id', 'display_archivo']
    
    
admin.site.register(actainicio, Actainicio)
#listar por tabla las acta de inicio en el panel de administracion

#prueba de listar por tabla de pruebas
class Prueba(admin.ModelAdmin):
    list_display = ('nombreprueba', 'cedula',)
admin.site.register(prueba, Prueba)
#prueba de listar por tabla de pruebas

#listar por tabla planillas en el panel de administracion
class Pl(admin.ModelAdmin):
    #aqui debe ir el nombre de la persona que pago
    list_display= ('numero', 'fecha','valortotal','usuario_id')
admin.site.register(planilla, Pl)
#listar por tabla planillas en el panel de administracion

#lista por tabla las actividades en panel de administracion
class Actividades(admin.ModelAdmin):
    #aqui debe ir el nombre de la persona que pasa las actvidades
    list_display= ('objeto','lugar','fecha','usuario_id')
admin.site.register(actividades, Actividades)
#lista por tabla las actividades en panel de administracion

#listar por tabla las actas de pago en el panel de administracion
class Ap(admin.ModelAdmin):
    #aqui debe ir el nombre de quien pasa el acta de pago
    list_display=('objeto', 'periodo', 'lugar', 'valor','usuario_id')
admin.site.register(actapago, Ap)
#listar por tabla las actas de pago en el panel de administracion

#listar por tabla las actividades en el panel de administracion
class Cseguimiento(admin.ModelAdmin):
    #Nombre o cedula de la persona a quien pertenece el certificado de seguimiento
    list_display=('numerocontrato', 'objeto', 'numerocuentapago','periodo','usuario_id')
admin.site.register(certificadoseguimiento, Cseguimiento)
#listar por tabla las actividades en el panel de administracion

#cuenta a pasar por el usuario
class Cuentausuario(admin.ModelAdmin):
    list_display=('email','cedula')
admin.site.register(cuentausuario, Cuentausuario)
#cuenta a pasar por el usuario

class CuentaBancaria(admin.ModelAdmin):
    list_display=('numero','tipocuenta','nombrecb','usuario_id')
admin.site.register(cuentabancaria, CuentaBancaria)

class CuentaContratista(admin.ModelAdmin):
    list_display=('id','numeroplanilla','archivo','objetocontrato','cedula')
admin.site.register(cuentacontratista, CuentaContratista )