import os.path
import os
import environ
from decouple import config
from unipath import Path

# from os.path import abspath, basename, dirname, join, normpath
# from sys import path
PROJECT_DIR = Path(__file__).parent.parent.parent
STATIC_URL = '/static/'


# The STATIC_ROOT variable in settings.py defines the single folder you want 
# to collect all your static files into. Typically, this would be a top-level
# folder inside your project
STATIC_ROOT = os.path.join(PROJECT_DIR,'static')


MEDIA_DIR = os.path.join(PROJECT_DIR,'/media')
MEDIA_ROOT = os.path.join(PROJECT_DIR,'media')
MEDIA_URL = '/media/'

ROOT_DIR = PROJECT_DIR

POSTS_TEMPLATE_DIR = os.path.join(PROJECT_DIR, 'posts/templates')
CONTACTME_TEMPLATE_DIR = os.path.join(PROJECT_DIR, 'contactme/templates')

CKEDITOR_UPLOAD_PATH = STATIC_ROOT
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'in-post_images/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins' : 'image2,imageresponsive',
        'removePlugins' : 'image',
    }

}

env = environ.Env(
    DEBUG=(bool, False),
)

environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')



MPTT_ADMIN_LEVEL_INDENT = 20

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', #provides access to the provided authentication systemm
    'django.contrib.contenttypes', # used by the auth app to track models installed in your database.
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'social_django',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',
    'django_archive',
    'contactme',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [POSTS_TEMPLATE_DIR, CONTACTME_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # <-- to process media files
                'social_django.context_processors.backends',  # <-- for OAuth
                'social_django.context_processors.login_redirect', # <-- for OAuth
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
            'OPTIONS': {'min_length': 6, }

    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    )


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dave@davemellor.com' 
EMAIL_HOST_PASSWORD = 'gcgeybmdrgdlwqtv'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

