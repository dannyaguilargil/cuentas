from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
import pymysql
pymysql.install_as_MySQLdb()

# Esto asegurará que Celery se cargue cuando Django se cargue
__all__ = ('celery_app',)