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
MEDIA_ROOT = os.path.join(BASE_DIR, 'pdfs')




########################################################

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ruhs)hlt#vqu=c)(n_tr$w__wpn2$!h!-=a+k=ts1ql0of)^kn'

# SECURITY WARNING: don't run with debug turned on in production!
#cuando la pose a produccion dejarlo en false
DEBUG = True

ALLOWED_HOSTS = [] #direcciones que tiene permitido consultar al servidor


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_usuarios', #agregues esta ruta
    'sistemas_cuentas',
    'gestion_supervisor',
    'gestion_presupuesto',
    'gestion_tesoreria',
    'django_datatables_view',
   # 'sistemas_cuentas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',#lo agrege por el idioma
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
       # 'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': BASE_DIR / 'db.sqlite3',
       
       #mysql -hcontainers-us-west-22.railway.app -uroot -ptkxWbDzZbbir7scaKl5G --port 7829 --protocol=TCP railway
       #mis creacciones para conexion con railway
       #'ENGINE': 'django.db.backends.mysql',
       #'NAME': 'railway',
       #'USER': 'root',
       #'PASSWORD': 'tkxWbDzZbbir7scaKl5G',
       #'HOST': 'containers-us-west-22.railway.app',
       #'PORT': '7829',
       
       
       #conexion con la base de datos local
       ###################################
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'sistema_cuentas',
       'USER': 'danny',
       'PASSWORD': 'danny',
       'HOST': 'localhost',
       'PORT': '3306',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-es' #estaba en en-us

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
#AGREGAR LA RUTA ACTUAL DONDE SE ENCUENTRA LA CARPETA
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'sistemas_cuentas/static'),)


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
