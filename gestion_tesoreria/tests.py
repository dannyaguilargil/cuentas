from django.test import TestCase
from gestion_tesoreria.models import cuentatesoreria

class CuentatesoreriaTesting(TestCase):
    def setUp(self):
        self.cuenta_tesoreria = cuentatesoreria.objects.create(
            nombre="Danny",
            segundonombre="Stiveens",
            primerapellido="Aguilar",
            segundoapellido="Gil",
            email="sistemas.acceso@imsalud.gov.co",
            supervisor="Lucas Augusto Liendo Romero",
            tipodocumento="CC",
            cedula=123456789,
            dependencia="Sistemas",
            sexo="M",
            numero=1234,
            objeto="Apoyo a la gestion en control de acceso",
            fechaperfeccionamiento="2023-06-01",
            valor="1000000",
            fechacontrato="2023-06-01",
            fechaterminacion="2023-12-31",
            duracion="6 meses",
            numerorp=5678,
            fecharp="2023-06-15",
            numeroactainicio=9012,
            fechaactainicio="2023-06-01",
            radicado="Radicado",
            validacionsupervisor="Aprobado",
            observacionessupervisor="Aprobado",
            ordendepago="Ord-01",
            comprobanteegreso="C-001"
        )

    def test_nombre_field(self):
        self.assertEqual(self.cuenta_tesoreria.nombre, "Danny")

    def test_cedula_field(self):
        self.assertEqual(self.cuenta_tesoreria.cedula, 123456789)

    def test_numero_field(self):
        self.assertEqual(self.cuenta_tesoreria.numero, 1234)

    def test_objeto_field(self):
        self.assertEqual(self.cuenta_tesoreria.objeto, "Apoyo a la gestion en control de acceso")

    
