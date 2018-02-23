from .base import *
# python manage.py migrate --settings=blog.settings.production

ALLOWED_HOSTS = ['www.nomadpad.io']

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

