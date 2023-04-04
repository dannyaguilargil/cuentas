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
       
    def __str__(self):
        return 'SOLICITUD DE USUARIO: ' + self.nombre + ' ' + self.apellido
      
       
#QUIERO HACER LA PARTE PRIMERO DE MOSTRAR LOS USUARIOS REGISTRADOS Y INCLUIR USUARIOS REGISTRADOS EN EL ADMIN
class usuario(models.Model):
    nombre = models.CharField(max_length=40)
    segundonombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    segundoapellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    supervisor = models.CharField(max_length=40)
    tipodocumento = models.CharField(max_length=40)
    cedula = models.IntegerField(primary_key=True)
    ##hast aqui va el de usuarios registrados
    lugarexpedicion = models.CharField(max_length=40)
    dependencia = models.CharField(max_length=40)
    sexo = models.CharField(max_length=40)
    usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=40)
    rol = models.CharField(max_length=40)
    

    #def __str__(self):
     #   return 'USUARIO: ' + self.nombre + ' ' + self.apellido
    
    
#class prueba(models.Model):
#    nombre = models.CharField(max_length=40)
#    cedula = models.IntegerField(primary_key=True)