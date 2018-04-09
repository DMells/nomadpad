"""Development settings and globals."""
from .base import *
# python manage.py runserver --settings=blog.settings.development

# Used the below website to create bash commands (GO)
# But instead of where is says gedit, type sublime
# http://www.djangopaths.com/creating-terminal-command-start-your-django-project/

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
