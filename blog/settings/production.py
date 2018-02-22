from .base import *
# python manage.py migrate --settings=mysite.settings.production

DEBUG = False

ALLOWED_HOSTS = ['www.nomadpad.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nomadpaddb',
        'USER': 'super',
        'PASSWORD': 'lalalala',
        'HOST': 'DMells123-678.postgres.pythonanywhere-services.com',
        'PORT':'10678',
    }
}

