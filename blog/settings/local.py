"""Development settings and globals."""
from .base import *
# python manage.py runserver --settings=blog.settings.development

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nomadpaddb',
        'USER': 'super',
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT':'',

    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'travelblogdb',
#         'USER': 'dmells',
#         'PASSWORD': 'comeonffs',
#         'HOST': 'localhost',
#         'PORT':'',

#     }
# }