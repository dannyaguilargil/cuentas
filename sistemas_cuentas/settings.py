"""
Django settings for sistemas_cuentas project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os #lo agregue
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#################PARA EL MANEJO DE PDFS###################
MEDIA_ROOT = os.path.join(BASE_DIR, 'sistemas_cuentas/static/') #desde static
MEDIA_URL = 'sistemas_cuentas/static/'
##MEDIA_ROOT = os.path.join(BASE_DIR, 'sistemas_cuentas/') ##directamente desde la carpeta media
#MEDIA_URL = 'sistemas_cuentas/'
######lo agregue
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
#TESSERACT_PATH = 'C:\Program Files\Tesseract-OCR'  # Reemplaza con la ruta correcta en tu sistema

########################################################

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ruhs)hlt#vqu=c)(n_tr$w__wpn2$!h!-=a+k=ts1ql0of)^kn'

# SECURITY WARNING: don't run with debug turned on in production!
#cuando la pose a produccion dejarlo en false
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.130','saradev.imsalud.gov.co','localhost','127.0.0.1','192.168.134.223']


# Application definition

INSTALLED_APPS = [
    'admin_interface', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_usuarios',
    'sistemas_cuentas',
    'gestion_supervisor',
    'gestion_presupuesto',
    'gestion_tesoreria',
    'gestion_identidades',
    'gestion_bitacora',
    'gestion_apis',
    'gestion_informes',
    'django_datatables_view',
    'filebrowser',
    'colorfield',
    'rest_framework', # apis
    'corsheaders', # apis
    'django_celery_results',
    'gestion_encuestas',
    #'django_admin_logs',
    #'django_celery_beat' opcional mas adelante
  
]

X_FRAME_OPTIONS = 'SAMEORIGIN' #PARA CAMBIAR ESTILOS AL PANEL ADMIN

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',#lo agrege por el idioma
    #'filebrowser.middleware.FileBrowserMiddleware',
]

ROOT_URLCONF = 'sistemas_cuentas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,"templates"], #ubicacion de templates para cargue de plantillas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sistemas_cuentas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
#mysql -hcontainers-us-west-22.railway.app -uroot -ptkxWbDzZbbir7scaKl5G --port 7829 --protocol=TCP railway
DATABASES = {
    'default': {
       
       #conexion con la base de datos local
       ###################################
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'sarav1',
       'USER': 'danny',
       'PASSWORD': 'danny',
       'HOST': 'localhost',
       'PORT': '3306',
       
    
}}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'es-es' #estaba en en-us

TIME_ZONE = 'America/Lima' ##'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'sistemas_cuentas/static'),)


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = []


EMAIL_BACKEND =
EMAIL_HOST =
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD =
EMAIL_PORT =
EMAIL_USE_SSL =
DEFAULT_FROM_EMAIL =

###########configuraciones necesaria para la tareas programadas #########
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//' 
CELERY_TIMEZONE = 'America/Lima'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
#####################################
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ENABLE_UTC = False
CELERY_BROKER_HEARTBEAT = 120  
CELERY_BROKER_CONNECTION_TIMEOUT = 60
CELERY_TASK_ACKS_LATE = True 
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERY_WORKER_PREFETCH_MULTIPLIER = 1 
###########LOGIN#####################
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = '/login'
###agregado para las sesiones
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600  
###########LOGIN#####################
