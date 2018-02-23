from .base import *

# python manage.py migrate --settings=blog.settings.production

DEBUG = False

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



########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = config('SECRET_KEY')
########## END SECRET CONFIGURATION

ALLOWED_HOSTS = ['www.nomadpad.io']