from django.db import models
from gestion_usuarios.choices import sexos, rol, tipodocumento

class cuentapresupuesto(models.Model):
    ############REVISAR QUE TENGAN LOS MISMOS DATOS QUE EL ANTERIOR##############################
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor')
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    cedula = models.IntegerField(verbose_name='Cedula')#llevarlo por id de cuenta y relacionarlo con usuario
    dependencia = models.CharField(max_length=40, verbose_name='Dependencia')
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F')
    #gestion de contratacion, tener en cuenta el pdf
    numero = models.IntegerField(verbose_name='Numero del contrato')
    objeto = models.CharField(max_length=300, verbose_name='Objeto') # este objeto de contrato debe remplazar al cargo en usuario
    fechaperfeccionamiento = models.CharField(max_length=300, verbose_name='Fecha de perfeccionamiento')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    fechacontrato = models.CharField(max_length=40, verbose_name='Fecha del contrato')
    fechaterminacion = models.CharField(max_length=40, verbose_name='Fecha final del contrato')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    #gestion de contratacion, tener en cuenta el pdf
    #gestion de rp, tener en cuenta el pdf
    numerorp = models.IntegerField(verbose_name='Numero del rp')
    fecharp = models.CharField(max_length=40, verbose_name='Fecha del rp')
    #gestion de rp, tener en cuenta el pdf
    #gestion de acta de inicio, tener en cuenta el pdf
    numeroactainicio = models.IntegerField(verbose_name='Numero proceso del acta de inicio')
    fechaactainicio = models.CharField(max_length=300, verbose_name='Fecha de acta de inicio')
    #gestiones del supervisor
    radicado = models.CharField(max_length=40, verbose_name='Radicado')
    validacionsupervisor = models.CharField(max_length=40, verbose_name='Validacion de la cuenta')
    observacionessupervisor = models.CharField(max_length=40, verbose_name='Observaciones de la cuenta')
    #gestiones de presupuesto
    ordendepago = models.CharField(max_length=40, verbose_name='Orden de pago')
    ################################################################
    ############        NO ACTIVIDADES     #########################
    ################################################################
