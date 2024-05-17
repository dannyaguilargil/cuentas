## archivo de configuracion de ejecuccion en segundo plano
## primero lo ejecuto desde raiz para una prueba con shell y luego lo acomodo en gestion_informes
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemas_cuentas.settings')

app = Celery('sistemas_cuentas')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.tasks(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')