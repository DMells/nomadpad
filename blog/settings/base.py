import os.path
from decouple import config
from unipath import Path

# from os.path import abspath, basename, dirname, join, normpath
# from sys import path
PROJECT_DIR = Path(__file__).parent.parent.parent
STATIC_URL = '/static/'

# App specific static files are stored in the static subdirectory 
# within the app. Django will also look in any directories listed in 
# the STATICFILES_DIRS setting. Let’s update our project settings to 
# specify a static files directory.
# STATICFILES_DIRS = [
#      os.path.join(PROJECT_DIR,'static'),
# ]
# The STATIC_ROOT variable in settings.py defines the single folder you want 
# to collect all your static files into. Typically, this would be a top-level
# folder inside your project
STATIC_ROOT = os.path.join(PROJECT_DIR,'static')


# MEDIA_DIR = os.path.join(PROJECT_DIR,'/media')
MEDIA_ROOT = os.path.join(PROJECT_DIR,'media')
MEDIA_URL = '/media/'

# ROOT_DIR = PROJECT_DIR

TEMPLATE_DIR = os.path.join(PROJECT_DIR, 'posts/templates')

CKEDITOR_UPLOAD_PATH = MEDIA_ROOT
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'in-post_images/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins' : 'image2',
        
    }
}

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = ["^@(z7s#9imf*xl+j%@i#%ftx_2mmb#%or(xnrccidj19&%c3(8"]
# SECRET_KEY = config('SECRET_KEY')

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



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', #provides access to the provided authentication systemm
    'django.contrib.contenttypes', # used by the auth app to track models installed in your database.
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'social_django',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',
    'django_archive',
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
        'DIRS': [TEMPLATE_DIR,],
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


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    )

