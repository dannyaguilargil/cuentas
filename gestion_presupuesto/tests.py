from django.test import TestCase
from gestion_presupuesto.models import cuentapresupuesto

class CuentapresupuestoTesting(TestCase):
    def setUp(self):
        self.cuenta_presupuesto = cuentapresupuesto.objects.create(
            nombre="Danny",
            segundonombre="Stiveens",
            primerapellido="Aguilar",
            segundoapellido="Gil",
            email="sistemas.acceso@gmail.com",
            supervisor="Lucas Augusto Liendo Romero",
            tipodocumento="CC",
            cedula=123456789,
            dependencia="Sistemas",
            sexo="M",
            numero=1234,
            objeto="Apoyo a la gestion del control de acceso",
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
            observacionessupervisor="Ninguna",
            ordendepago="Ord-01"
        )

    def test_nombre_field(self):
                self.assertEqual(self.cuenta_presupuesto.nombre, "Danny")

    def test_cedula_field(self):
                self.assertEqual(self.cuenta_presupuesto.cedula, 123456789)

    def test_numero_field(self):
                self.assertEqual(self.cuenta_presupuesto.numero, 1234)

    def test_objeto_field(self):
                self.assertEqual(self.cuenta_presupuesto.objeto, "Apoyo a la gestion del control de acceso")