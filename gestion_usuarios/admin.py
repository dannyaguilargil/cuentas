from django.contrib import admin
from .models import  usuario, usolicitudes, contrato, rp, actainicio, prueba, planilla, actividades, actapago, certificadoseguimiento

admin.site.site_header = "Administracion sistema de cuentas"
admin.site.site_title = "Administracion"
admin.site.index_title = "Bienvenido Administrador!"
# Register your models here.
admin.site.register(usolicitudes)
admin.site.register(usuario)
admin.site.register(contrato)
admin.site.register(rp)
admin.site.register(actainicio)
admin.site.register(prueba)
admin.site.register(planilla)
admin.site.register(actividades)
admin.site.register(actapago)
admin.site.register(certificadoseguimiento)
#debo agregar uno de prueba para revisar select y demas en modelos
