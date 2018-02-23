"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *
# python manage.py runserver --settings=blog.settings.development

DEBUG = True

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

