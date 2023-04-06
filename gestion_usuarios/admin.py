from django.contrib import admin
from .models import  usuario, usolicitudes, contrato, rp

# Register your models here.
admin.site.register(usolicitudes)
admin.site.register(usuario)
admin.site.register(contrato)
admin.site.register(rp)
