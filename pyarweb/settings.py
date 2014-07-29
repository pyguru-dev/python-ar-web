"""
Django settings for pyarweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c2*wzebi9p3vola_tamd7zu4=4(2^9m$v0vdj(5_ybhhw6t629'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Sites framework
SITE_ID = 1

TEMPLATE_DIRS = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DEBUG = True

# Instead of sending out real emails the console backend just writes
# the emails that would be sent to the standard output.
# By default, the console backend writes to stdout
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = []

# Django registration
# https://django-registration.readthedocs.org/en/latest/quickstart.html
ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL = 'webmaster@python.org.ar'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/pyarenses/login/'


# Disqus
DISQUS_API_KEY = '3t6eKCbxRGuIG3SmdHb8malOf1h2WxSYEfXbBjWyNBaFLMyD1GOIfWYFciqJqo69'
DISQUS_WEBSITE_SHORTNAME = 'PyAr'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # pyarweb apps
    'community',
    'news',
    'pycompanies',
    'jobs',
    'events',
    'newbie',
    'projects',
    'faq',

    # 3rd party apps
    'django_extensions',
    'registration',
    'disqus',
    'taggit',
    'taggit_autosuggest',
    'bootstrap3_datetime',
    'planet',
    'pagination',
    'tagging',
    'bootstrap3',
    'django_summernote',
    'south',
    'crispy_forms',
    'email_obfuscator',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'pyarweb.urls'

WSGI_APPLICATION = 'pyarweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Activa todo el sitio con el horario de Argentina
# from django.utils import timezone
# timezone.activate(TIME_ZONE)

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.contrib.messages.context_processors.messages",
    "planet.context_processors.context"
)

PLANET = {"USER_AGENT": "pyarweb/0.1"}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SUMMERNOTE_CONFIG = {
    'inplacewidget_external_css': (),
}