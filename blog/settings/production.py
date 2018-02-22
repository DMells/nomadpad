from .base import *
# python manage.py migrate --settings=blog.settings.production

DEBUG = False

ALLOWED_HOSTS = ['www.nomadpad.io']

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nomadpaddb',
        'USER': 'super',
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'DMells123-678.postgres.pythonanywhere-services.com',
        'PORT':'10678',
    }
}

