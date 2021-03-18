import os
import environ
from pathlib import Path
from django.core.management.utils import get_random_secret_key

env = environ.Env()

ENV_FILE = env.str('ENV_FILE', default='.env')

environ.Env.read_env(env_file=ENV_FILE)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = env.bool('DEBUG', default=False)

SECRET_KEY = env.str('SECRET_KEY', default=get_random_secret_key())

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'common',
    'broker'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'common.User'

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [
    BASE_DIR / 'templates'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env.str('DATABASES_NAME'),
#         'USER': env.str('DATABASES_USER'),
#         'PASSWORD': env.str('DATABASES_PASSWORD'),
#         'HOST': env.str('DATABASES_HOST'),
#         'PORT': env.str('DATABASES_PORT'),
#     }
# }

STATIC_URL = '/staticfiles/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = []

MEDIA_URL = '/mediafiles/'

MEDIA_ROOT = BASE_DIR / 'mediafiles'

CELERY_BROKER_URL = os.environ.get('BROKER_HOST', 'amqp://localhost')
