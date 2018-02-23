# https://github.com/wooyek/django-settings-strategy
import logging
import environ

logging.debug("Settings loading: %s" % __file__)

# This will read missing environment variables from a file
# We wan to do this before loading a base settings as they may depend on environment
environ.Env.read_env(DEBUG='True')

from .base import *
# python manage.py runserver --settings=blog.settings.development

ALLOWED_HOSTS += [
    '127.0.0.1',
    'localhost',
    '.example.com',
    ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travelblogdb',
        'USER': 'dmells',
        'PASSWORD': 'comeonffs',
        'HOST': 'localhost',
        'PORT':'',

    }
}

