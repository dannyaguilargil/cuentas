from django.test import TestCase
from gestion_usuarios.models import usolicitudes,usuario,contrato,rp,actainicio,planilla

class UsolicitudesModelTestCase(TestCase):
    def setUp(self):
        self.usolicitud = usolicitudes.objects.create(
            nombre="Danny",
            segundonombre="Stiveens",
            primerapellido="Aguilar",
            segundoapellido="Gil",
            cargo="Desarollador",
            email="sistemas.acceso@imsalud.gov.co",
            supervisor="Lucas Augusto Liendo Romero",
            tipodocumento="CC",
            cedula=109049237
        )

    def test_nombre_field(self):
        self.assertEqual(self.usolicitud.nombre, "Danny")

    def test_cedula_field(self):
        self.assertEqual(self.usolicitud.cedula, 109049237)
        
        
    
class UsuarioTesting(TestCase):
    def setUp(self):
        self.usuario = usuario.objects.create(
            nombre="Danny",
            segundonombre="Stiveens",
            primerapellido="Aguilar",
            segundoapellido="Gil",
            cargo="Desarollador",
            email="sistemas.acceso@imsalud.gov.co",
            supervisor="Supervisor",
            tipodocumento="CC",
            cedula=109049237,
            lugarexpedicion="Cucuta",
            dependencia="Sistemas",
            sexo="M",
            usuario="daguilar",
            contrasena="imsaludfirme",
            telefono=5813604,
            direccion="Calle 9na #10-64 motilones",
            rol="Contratista"
        )

    def test_nombre_field(self):
        self.assertEqual(self.usuario.nombre, "Danny")

    def test_cedula_field(self):
        self.assertEqual(self.usuario.cedula, 109049237)
        
class ContratoTesting(TestCase):
    def setUp(self):
        self.contrato = contrato.objects.create(
            numero=1234,
            numeroproceso=5678,
            objeto='Apoyo a la gestion de desarollo de la E.S.E. IMSALUD',
            fechaperfeccionamiento='2023-06-15',
            valor='1000000',
            fechacontrato='2023-06-15',
            fechaterminacion='2024-06-15',
            duracion='12 meses',
            supervisor='Lucas Augusto Liendo Romero',
            archivo='ruta/al/archivo.pdf'
        )

    def test_numero_field(self):
        self.assertEqual(self.contrato.numero, 1234)

    def test_objeto_field(self):
        self.assertEqual(self.contrato.objeto, 'Apoyo a la gestion de desarollo de la E.S.E. IMSALUD')


class RPTesting(TestCase):
    def setUp(self):
        self.usuario = usuario.objects.create(
            nombre='Danny',
            primerapellido='Aguilar',
            cedula=1234567890
        )
        self.rp = rp.objects.create(
            numero=1234,
            fecha='2023-06-15',
            duracion='12 meses',
            valor='1000000',
            archivo='ruta/al/archivo.pdf',
            usuario=self.usuario
        )

    def test_numero_field(self):
        self.assertEqual(self.rp.numero, 1234)

    def test_fecha_field(self):
        self.assertEqual(self.rp.fecha, '2023-06-15')
        
    def test_usuario_relation(self):
        self.assertEqual(self.rp.usuario, self.usuario)
        
class ActaInicioTesting(TestCase):
    def setUp(self):
        self.usuario = usuario.objects.create(
            nombre='Danny',
            primerapellido='Aguilar',
            cedula=1234567890
        )
        self.acta = actainicio.objects.create(
            numero=1234,
            fecha='2023-06-15',
            duracion='12 meses',
            valor='1000000',
            archivo='ruta/al/archivo.pdf',
            usuario=self.usuario
        )

    def test_numero_field(self):
        self.assertEqual(self.acta.numero, 1234)

    def test_fecha_field(self):
        self.assertEqual(self.acta.fecha, '2023-06-15')

    def test_usuario_relation(self):
        self.assertEqual(self.acta.usuario, self.usuario)
        
class PlanillaTesting(TestCase):
    def setUp(self):
        self.usuario = usuario.objects.create(
            nombre='Danny',
            primerapellido='Aguilar',
            cedula=1234567890
        )
        self.planilla = planilla.objects.create(
            numero=1,
            fecha='2023-06-15',
            periodo='Junio 2023',
            valortotal='1000000',
            nombrepension='Porvenir',
            valorpension='100000',
            nombresalud='Nueva EPS',
            valorsalud='50000',
            nombrearl='SURA',
            valorarl='20000',
            archivo='ruta/al/archivo.pdf',
            usuario=self.usuario
        )

    def test_numero_field(self):
        self.assertEqual(self.planilla.numero, 1)

    def test_fecha_field(self):
        self.assertEqual(self.planilla.fecha, '2023-06-15')

    def test_usuario_relation(self):
        self.assertEqual(self.planilla.usuario, self.usuario)