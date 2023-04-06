from django.contrib import admin
from .models import  usuario, usolicitudes, contrato

# Register your models here.
admin.site.register(usolicitudes)
admin.site.register(usuario)
admin.site.register(contrato)

