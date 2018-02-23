from .base import *
# python manage.py runserver --settings=blog.settings.development

DEBUG=True

SECRET_KEY = config('SECRET_KEY')

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

