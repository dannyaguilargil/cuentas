from django.contrib import admin
from .models import  usuario, prueba, usolicitudes

# Register your models here.
admin.site.register(usolicitudes)
admin.site.register(usuario)
admin.site.register(prueba)

