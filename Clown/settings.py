#coding: utf-8

import os, sys
from path import path

ADMINS = (
    ('Tomasz Kopczuk', 'tomek@bladepolska.com'),
    ('Marcin Mincer', 'marcin@bladepolska.com')
)

MANAGERS = ADMINS

PROJECT_NAME = "Clown"
DOMAIN = "clown.herokuapp.com"

SERVE_STATIC_FILES = True

BROKER_URL = "%s/0" % os.environ.get('REDISTOGO_URL', 'redis://localhost/')


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

DEPLOY_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

LOG_FILE = os.path.join(os.path.join(DEPLOY_PATH, 'logs'), '%s.log' % PROJECT_NAME)

# Create a directory tree for the logfile if it doesnot exist yet.
from bladepolska.dirs import mkdir_p
mkdir_p(os.path.dirname(LOG_FILE))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(DEPLOY_PATH, 'user_uploads')
mkdir_p(os.path.dirname(MEDIA_ROOT))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(DEPLOY_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$r5*)alapqyd*#n*^pm3wew#e*^4yglf$&amp;(1y6wc#rpw(4e&amp;%5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    # 'bladepolska.context_processors.settings',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'bladepolska.middleware.InstrumentMiddleware',
    # 'bladepolska.middleware.SubdomainMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'bladepolska.middleware.SessionMiddlewareOmitApi',
    # 'bladepolska.middleware.CsrfViewMiddlewareOmitApi',
    # 'bladepolska.mobiletokenlogin.middleware.MobileAPITokenAuthenticationMiddleware',
    # 'bladepolska.middleware.AuthenticationMiddlewareOmitApi',
    # 'bladepolska.middleware.MessageMiddlewareOmitApi',
)

ROOT_URLCONF = 'Clown.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Clown.wsgi.application'

# AUTH_USER_MODEL = 'users.User'

TEMPLATE_DIRS = (
    os.path.join(DEPLOY_PATH, 'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'gunicorn',
    'south',
    'coffin',

    'Clown',
    'profiles',
    'tuitter'
)


# App settings
ACCOUNT_ACTIVATION_DAYS = 7



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)-12s] [%(levelname)s] %(message)s',
            'datefmt': '%b %d %H:%M:%S'
        },
        'simple': {
            'format': '%(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': '16777216',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'Clown': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

JINJA2_ENVIRONMENT_OPTIONS = {

}

JINJA2_EXTENSIONS = (
    'jinja2.ext.i18n',
    'jinja2.ext.loopcontrols',
)

import datetime
JINJA2_GLOBALS = {
    'getattr': getattr,
    'hasattr': hasattr,
    'filter': filter,
    'datetime': datetime.datetime,
    'unicode': unicode
}

#
# BLADE POLSKA BOILERPLATE REUSABLE PART BELOW
# DO NOT EDIT UNLESS YOU KNOW WHAT YOU'RE DOING
#

import smartsettings
smartsettings.config(globals(), {
    'FLAVOURS': (
        'TESTING',
        'DEV',
        'STAGING',
        'PRODUCTION',
    ),
    'DEFAULT': 'DEV'  # default flavour always loads localsettings.py!
})
