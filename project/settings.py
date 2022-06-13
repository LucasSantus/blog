from pathlib import Path
import os, sys

# Configuration Project
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    os.path.join(BASE_DIR, "apps")
)

SECRET_KEY = str(os.environ.get('SECRET_KEY', "django-insecure-900u2i6xbp12y#l7-%ch9h(w(jxj17n)c1btv1p=$6$iz27t7m"))

DEBUG = int(os.environ.get('DEBUG', 1))

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('*')

# Default Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Interns Apps
INSTALLED_APPS += [
    'home',
    'posts',
    'users',
]

# Externs Apps
INSTALLED_APPS += [
    "bootstrap5",
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': str(os.environ.get('DB_NAME', BASE_DIR / 'db.sqlite3')),
        'USER': str(os.environ.get('DB_USER', '')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD', '')),
        'HOST': str(os.environ.get('DB_HOST', '')),
        'PORT': str(os.environ.get('DB_PORT', ''))
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: False if request.is_ajax() else True,
    }

AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#SMTP
EMAIL_BACKEND = str(os.environ.get('EMAIL_BACKEND', "django.core.mail.backends.console.EmailBackend"))
EMAIL_HOST = str(os.environ.get('EMAIL_HOST', "smtp.gmail.com"))
EMAIL_PORT = str(os.environ.get('EMAIL_PORT', 587))
EMAIL_HOST_USER = str(os.environ.get('EMAIL_HOST_USER', ""))
EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_HOST_PASSWORD', ""))
EMAIL_USE_TLS = str(os.environ.get('EMAIL_USE_TLS', True))
DEFAULT_FROM_EMAIL = 'Blog'

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')