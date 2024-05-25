from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemas_cuentas.settings')

app = Celery('sistemas_cuentas')


# Leer la configuración desde la configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubrir y cargar las tareas definidas en los paquetes de apps registradas en Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')