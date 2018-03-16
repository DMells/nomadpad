from .base import *
from decouple import config
# python manage.py migrate --settings=blog.settings.production

DEBUG = False

# App specific static files are stored in the static subdirectory 
# within the app. Django will also look in any directories listed in 
# the STATICFILES_DIRS setting. Let’s update our project settings to 
# specify a static files directory.
# STATICFILES_DIRS = [
#       "/home/DMells123/nomadpad/media/in-post_images",
#       "/home/DMells123/nomadpad/media/primary_images",
#  ]

ALLOWED_HOSTS = ['www.nomadpad.io']

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key

# SECRET_KEY= config('SECRET_KEY')
########## END SECRET CONFIGURATION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nomadpaddb',
        'USER': 'super',
        'PASSWORD': 'lalalala',
        # 'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'DMells123-678.postgres.pythonanywhere-services.com',
        'PORT':'10678',
    }
}