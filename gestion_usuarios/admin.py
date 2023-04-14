from django.contrib import admin
from .models import  usuario, usolicitudes, contrato, rp, actainicio, prueba, planilla, actividades, actapago, certificadoseguimiento

#Modificaciones del frontend
admin.site.site_header = "Administracion sistema de cuentas"
admin.site.site_title = "Administracion"
admin.site.index_title = "Bienvenido Administrador!"
#Modificaciones del frontend


# Listar por tabla a solicitudes de usuarios
class Usolicitud(admin.ModelAdmin):
    list_display=('nombre', 'primerapellido', 'segundoapellido', 'cedula', 'cargo')
admin.site.register(usolicitudes, Usolicitud)
#Listar por tabla a solicitudes de usuarios

#listar por tablas usuarios
class User(admin.ModelAdmin):
    list_display= ('nombre', 'primerapellido', 'segundoapellido', 'cedula', 'rol')
admin.site.register(usuario, User)
# listar por tablas usuarios

#listar por tabla los contrato en el panel de administracion
class Cont(admin.ModelAdmin):
    #aqui debe ir el nombre de la persona que pertenece el contrato
    list_display=('numero', 'objeto', 'valor', 'duracion')
admin.site.register(contrato, Cont)
#listar por tabla los contrato en el panel de administracion


#listar por tablas usuarios
class Rps(admin.ModelAdmin):
    list_display= ('numero', 'fecha', 'duracion', 'valor')
admin.site.register(rp, Rps)
#listar por tablas usuarios

#listar por tabla las acta de inicio en el panel de administracion
class Actainicio(admin.ModelAdmin):
    #aqui va el nombe o cedula de la persona que pasa el acta de inicio
    list_display=('fecha','duracion', 'valor')
admin.site.register(actainicio, Actainicio)
#listar por tabla las acta de inicio en el panel de administracion

#prueba de listar por tabla de pruebas
class Prueba(admin.ModelAdmin):
    list_display = ('nombreprueba', 'cedula')
admin.site.register(prueba, Prueba)
#prueba de listar por tabla de pruebas

#listar por tabla planillas en el panel de administracion
class Pl(admin.ModelAdmin):
    #aqui debe ir el nombre de la persona que pago
    list_display= ('numero', 'fecha', 'nombrepension', 'nombresalud', 'valortotal')
admin.site.register(planilla, Pl)
#listar por tabla planillas en el panel de administracion

#lista por tabla las actividades en panel de administracion
class Actividades(admin.ModelAdmin):
    #aqui debe ir el nombre de la persona que pasa las actvidades
    list_display= ('objeto','lugar','fecha')
admin.site.register(actividades, Actividades)
#lista por tabla las actividades en panel de administracion

#listar por tabla las actas de pago en el panel de administracion
class Ap(admin.ModelAdmin):
    #aqui debe ir el nombre de quien pasa el acta de pago
    list_display=('objeto', 'periodo', 'lugar', 'valor')
admin.site.register(actapago, Ap)
#listar por tabla las actas de pago en el panel de administracion


#listar por tabla las actividades en el panel de administracion
class Cseguimiento(admin.ModelAdmin):
    #Nombre o cedula de la persona a quien pertenece el certificado de seguimiento
    list_display=('numerocontrato', 'objeto', 'numerocuentapago','periodo')
admin.site.register(certificadoseguimiento, Cseguimiento)
#listar por tabla las actividades en el panel de administracion

