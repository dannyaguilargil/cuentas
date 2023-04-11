from django.db import models


# Create your models here.
#class solicitud_usuario(models.Model):
#    nombre = models.CharField(max_length=40)
#    segundonombre = models.CharField(max_length=40)
#    primerapellido = models.CharField(max_length=40)
#    segundoapellido = models.CharField(max_length=40)
#    cargo = models.CharField(max_length=40)
#    email = models.CharField(max_length=40)
#    supervisor = models.CharField(max_length=40)
#    tipodocumento = models.CharField(max_length=40)
#    cedula = models.IntegerField(primary_key=True)
       
#    class Meta:
#        db_table = 'usolicitud'   
       
#    def __str__(self):
#        return 'SOLICITUD DE USUARIO: ' + self.nombre + ' ' + self.primerapellido
      
       
#QUIERO HACER LA PARTE PRIMERO DE MOSTRAR LOS USUARIOS REGISTRADOS Y INCLUIR USUARIOS REGISTRADOS EN EL ADMIN
class usuario(models.Model):
    #sexo = (
     #   ('M', 'Masculino'),
     #   ('F', 'Femenino'),
    #)
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    cargo = models.CharField(max_length=40, verbose_name='Cargo')
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor')
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento')
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula')
    ##hast aqui va el de usuarios registrados
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion')
    dependencia = models.CharField(max_length=40, verbose_name='Dependencia')
    sexo = models.CharField(max_length=40, verbose_name='Sexo')
    usuario = models.CharField(max_length=40, verbose_name='Usuario')
    contrasena = models.CharField(max_length=40, verbose_name='Contrasena')
    rol = models.CharField(max_length=40, verbose_name='Rol')
    

    def __str__(self):
        return 'USUARIO: ' + self.nombre + ' ' + self.primerapellido
    
    
class prueba(models.Model):
    nombreprueba = models.CharField(max_length=40)
    cedula = models.IntegerField(primary_key=True)
    
    
    
class usolicitudes(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    cargo = models.CharField(max_length=40, verbose_name='Cargo')
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor')
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento')
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula')

       
    def __str__(self):
        return 'SOLICITUD DE USUARIO: ' + self.nombre + ' ' + self.primerapellido
    
#por ahora solo quiero hacer registros pero debo referenciarlo con llave foranea
class contrato(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero')
    numeroproceso = models.IntegerField(verbose_name='Numero de proceso')
    objeto = models.CharField(max_length=300, verbose_name='Objeto')
    #fechasuscripcion = models.CharField(max_length=300, verbose_name='Fecha de suscripcion')
    fechaperfeccionamiento = models.CharField(max_length=300, verbose_name='Fecha de perfeccionamiento')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    fechacontrato = models.CharField(max_length=300, verbose_name='Fecha del contrato')
    fechaterminacion = models.CharField(max_length=300, verbose_name='Fecha final del contrato')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    #pendiente asignar llave foranea aqui
    def __str__(self):
        return 'CONTRATO: '+self.objeto
    
class rp(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero del rp')
    fecha = models.CharField(max_length=300, verbose_name='Fecha del rp')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    #pendiente asignar llave foranea aqui
    def __str__(self):
        return 'REGISTRO PRESUPUESTAL: '+self.fecha
    
class actainicio(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero del proceso')
    fecha = models.CharField(max_length=300, verbose_name='Fecha de acta de inicio')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    
    def __str__(self):
        return 'ACTA DE INICIO: '+self.fecha
 
#gestion de documentos del usuario    
class planilla(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero de la planilla')
    fecha = models.CharField(max_length=300, verbose_name='Fecha del pago de la planilla')
    periodo = models.CharField(max_length=40, verbose_name='Periodo de la planilla')
    valortotal = models.CharField(max_length=300, verbose_name='Valor total de la planilla')
    nombrepension = models.CharField(max_length=300, verbose_name='Nombre de la entidad de pension')
    valorpension = models.CharField(max_length=300, verbose_name='Valor de la pension')
    nombresalud = models.CharField(max_length=300, verbose_name='Nombre de la entidad de salud')
    valorsalud = models.CharField(max_length=300, verbose_name='Valor de la salud')
    nombrearl = models.CharField(max_length=300, verbose_name='Nombre de la entidad de arl')
    valorarl = models.CharField(max_length=300, verbose_name='Valor de arl')

    def __str__(self):
        return 'PLANILLA: '+self.periodo
    
class actividades(models.Model):
    objeto = models.CharField(max_length=300, verbose_name='Objeto del contrato')
    lugar = models.CharField(max_length=40, verbose_name='Lugar donde realizo la actividad')
    fecha = models.CharField(max_length=40, verbose_name='Fecha de la cuenta')
    actividades = models.CharField(max_length=600, verbose_name='Actividades a realizar ')
    resultadoactvidades = models.CharField(max_length=600, verbose_name='Resultado de las actividades')

    def __str__(self):
        return 'ACTA DE INICIO: '+self.objeto
    
class actapago(models.Model):
    objeto = models.CharField(max_length=300, verbose_name='Objeto del contrato')
    lugar = models.CharField(max_length=40, verbose_name='Lugar donde realizo la actividad')
    valor = models.CharField(max_length=40, verbose_name='Valor del contrato')
    fechaperfeccionamiento = models.CharField(max_length=40, verbose_name='Fecha de perfeccionamiento')
    numeroacta = models.IntegerField(verbose_name='Numero de acta de pago')
    fechacuenta = models.CharField(max_length=600, verbose_name='Fecha en la que pasa la cuenta') #aqui tomar el mes automaticamente y dia
    periodo = models.IntegerField( verbose_name='Periodo de pago')

    def __str__(self):
        return 'ACTA DE PAGO: '+self.objeto
    
class certificadoseguimiento(models.Model):
    numerocontrato = models.IntegerField( verbose_name='Numero del contrato')
    fechacuenta = models.CharField(max_length=40, verbose_name='Fecha actual de la cuenta')
    objeto = models.CharField(max_length=40, verbose_name='Objeto del contrato')
    rp = models.CharField(max_length=40, verbose_name='Numero del registro presupuestal')
    fechasuscripcion = models.CharField(max_length=40, verbose_name='Fecha de suscripcion del contrato')
    fechaterminacion = models.CharField(max_length=40,verbose_name='Fecha terminacion del contrato')
    periodo = models.IntegerField( verbose_name='Periodo de pago')
    numeroplanilla = models.IntegerField( verbose_name='Numero de planilla de pago')
    nombresalud = models.CharField(max_length=40,verbose_name='Nombre de la entidad de salud')
    valorsalud = models.CharField(max_length=40,verbose_name='Valor de la salud')
    nombrepension = models.CharField(max_length=40,verbose_name='Nombre de la entidad de pension')
    valorpension = models.CharField(max_length=40,verbose_name='Valor de la entidad de pension')
    nombrearl = models.CharField(max_length=40,verbose_name='Nombre de la entidad de arl')
    valorarl = models.CharField(max_length=40,verbose_name='Valor de la entidad de arl')
    cuentapago = models.CharField(max_length=40,verbose_name='Nombre de la entidad bancaria')
    numerocuentapago = models.IntegerField( verbose_name='Numero de la entidad bancaria')

    def __str__(self):
        return 'ACTA DE PAGO: '+self.objeto