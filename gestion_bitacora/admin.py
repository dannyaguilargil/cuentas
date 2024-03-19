from django.contrib import admin
from .models import bitacora

class bitacoraActividades(admin.ModelAdmin):
    list_display=('titulo', 'descripcion')
    search_fields = ('titulo',)
admin.site.register(bitacora, bitacoraActividades)
