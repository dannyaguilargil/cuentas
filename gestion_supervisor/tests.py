from django.test import TestCase
from gestion_supervisor.models import cuentasupervisor

class CuentasupervisorModelTestCase(TestCase):
    def setUp(self):
        self.cuenta_supervisor = cuentasupervisor.objects.create(
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
            objeto="Apoyo a la gestion de desarollador",
            fechaperfeccionamiento="2023-06-01",
            valor="1000000",
            fechacontrato="2023-06-01",
            fechaterminacion="2023-12-31",
            duracion="6 meses",
            numerorp=5678,
            fecharp="2023-06-15",
            numeroactainicio=9012,
            fechaactainicio="2023-06-01",
            radicado="RAD-01",
            validacionsupervisor="APROBADO",
            observacionessupervisor="NINGUNA"
        )

    def test_nombre_field(self):
        self.assertEqual(self.cuenta_supervisor.nombre, "Danny")

    def test_cedula_field(self):
        self.assertEqual(self.cuenta_supervisor.cedula, 123456789)