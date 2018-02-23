import environ
# https://github.com/wooyek/django-settings-strategy

from .base import *
# python manage.py migrate --settings=blog.settings.production
environ.Env.read_env(path(__file__) / "production.env", DEBUG='False', ASSETS_DEBUG='False')
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

