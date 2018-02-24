from .base import *
from decouple import config
# python manage.py migrate --settings=blog.settings.production

DEBUG = False



ALLOWED_HOSTS = ['www.nomadpad.io']

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = config('SECRET_KEY')
########## END SECRET CONFIGURATION
