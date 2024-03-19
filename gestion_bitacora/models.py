from django.db import models

class bitacora(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    realizado = models.BooleanField(default=False)
