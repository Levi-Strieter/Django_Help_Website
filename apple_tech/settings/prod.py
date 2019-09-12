from .base import *
import django_heroku
import dj_database_url
import dotenv

INSTALLED_APPS = [
    'core',
    'website',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DEBUG = False
ALLOWED_HOSTS = ['*']

# Activate Django-Heroku.
django_heroku.settings(locals())


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


LOGIN_REDIRECT_URL = '/core/dashboard'


#heroku production postgres stuff
# This line should already exist in your settings.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

