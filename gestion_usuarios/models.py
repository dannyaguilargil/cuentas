from django.db import models

# Create your models here.
class solicitud_usuario(models.Model):
    nombre = models.CharField(max_length=40)
    segundonombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    segundoapellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    supervisor = models.CharField(max_length=40)
    tipodocumento = models.CharField(max_length=40)
    cedula = models.IntegerField(primary_key=True)
    
#class prueba(models.Model):
#    nombre = models.CharField(max_length=40)
#    cedula = models.IntegerField(primary_key=True)