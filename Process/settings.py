"""
Django settings for Process project.
 
Generated by 'django-admin startproject' using Django 3.2.
 
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
 
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
 
from dotenv import load_dotenv

from pathlib import Path
import os
import mimetypes
mimetypes.add_type("text/css", ".css", True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)h%e!%l-y9+j%v14!j@-3gh@(-!7579(4hz8l6e%147w9_j@mz'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
 
 
# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    "crispy_forms",
    "crispy_bootstrap5",
]
 ## Template Crisp
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
 
ROOT_URLCONF = 'Process.urls'
 
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

#CONFIGURACION CORREO ELECTRONICO
EMAIL = os.getenv('EMAIL')
PASSWD = os.getenv('PASSWD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL  #DIRECCION DE CORREO ELECTRONICO
EMAIL_HOST_PASSWORD = PASSWD #PASSWORD DEL CORREO ELECTRONICO
EMAIL_FILE_PATH = '/tmp/' # change this to a proper location


RUTA = os.getenv('RUTA')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [RUTA],
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
 
WSGI_APPLICATION = 'Process.wsgi.application'
 
 
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
 
""" Futura Config Oracle
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/XEPDB1',
        'USER': 'arij',
        'PASSWORD': '123',
        'TEST': {
            'USER': 'default_test',
            'TBLSPACE': 'default_test_tbls',
            'TBLSPACE_TMP': 'default_test_tbls_tmp',
        },
    },
}
"""
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/XEPDB1',
        'USER': 'arij',
        'PASSWORD': '123',
        'TEST': {
            'USER': 'default_test',
            'TBLSPACE': 'default_test_tbls',
            'TBLSPACE_TMP': 'default_test_tbls_tmp',
        },
    },
}
 
 
 
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
 
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

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

 
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
 
LANGUAGE_CODE = 'es' #en-us
 
TIME_ZONE = 'Etc/GMT-3'
 
USE_I18N = True
 
USE_L10N = True
 
USE_TZ = True
 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
 
STATIC_URL = '/static/'
 
MEDIA_URL = '/img/'
 
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/img')
 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
 
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
#DataFlair #Local Memory Cache
'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'DataFlair',
    }
} 
'''