from .base import *

DEBUG = False

ALLOWED_HOSTS = ['www.nomadpad.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nomadpaddb',
        'USER': 'super',
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('HOST'),
        'PORT':env('PORT'),
    }
}