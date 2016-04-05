# coding=utf-8
# Copyright 2016 Materiality Labs.

from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)

import logging.config
import os


SITE_ID = 1

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Set up logging without allowing Django to add its defaults, as they are notoriously difficult to override properly.

LOGGING_CONFIG = None

LOGGING = {
  'version': 1,
  'formatters': {
    'default': {
      'format': '[%(asctime)s %(levelname)s %(pathname)s:%(lineno)s] %(message)s',
      'datefmt': '%Y-%m-%d %H:%M:%S'
    }
  },
  'handlers': {
    'console': {
      'class': 'logging.StreamHandler',
      'level': 'INFO',
      'formatter': 'default'
    }
  },
  'loggers': {
    # Everything will propagate to the root logger.  Note that the special name 'root' represents the logger at
    # the root of the dotted-string hierarchy, and which you'd logically expect to be represented by an empty string.
    'root': {
      'handlers': ['console'],
      'level': 'WARNING'
    },
    'django': {
      'handlers': ['console'],
      'level': 'INFO'
    },
    'allauth': {
      'handlers': ['console'],
      'level': 'INFO'
    },
    'dicpick': {
      'handlers': ['console'],
      'level': 'INFO'
    },
    'django.db.backends': {
      'handlers': ['console'],
      'level': 'INFO'  # Set to DEBUG to see live SQL queries.
    },
  }
}

logging.config.dictConfig(LOGGING)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
  # First in the list, so it can overide the standard collectstatic command.
  'materiality.django.static',

  # These must come before django.contrib.admin.
  'admin_tools',
  'admin_tools.theming',
  'admin_tools.menu',
  'admin_tools.dashboard',

  # The admin_tools_stats admin_tools module.
  'django_nvd3',
  'admin_tools_stats',

  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  #'debug_toolbar',
  #'pympler',

  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'allauth.socialaccount.providers.twitter',

  'dicpick',
)

DEBUG_TOOLBAR_PANELS = [
  'debug_toolbar.panels.versions.VersionsPanel',
  'debug_toolbar.panels.timer.TimerPanel',
  'debug_toolbar.panels.settings.SettingsPanel',
  'debug_toolbar.panels.headers.HeadersPanel',
  'debug_toolbar.panels.request.RequestPanel',
  'debug_toolbar.panels.sql.SQLPanel',
  'debug_toolbar.panels.staticfiles.StaticFilesPanel',
  'debug_toolbar.panels.templates.TemplatesPanel',
  'debug_toolbar.panels.cache.CachePanel',
  'debug_toolbar.panels.signals.SignalsPanel',
  'debug_toolbar.panels.logging.LoggingPanel',
  'debug_toolbar.panels.redirects.RedirectsPanel',
  #'debug_toolbar.panels.profiling.ProfilingPanel',  # TODO: Breaks admin. Figure out why.
  #'pympler.panels.MemoryPanel',
]

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',
)

AUTHENTICATION_BACKENDS = (
  # Needed to login by username in Django admin, regardless of allauth.
  'django.contrib.auth.backends.ModelBackend',
  # allauth-specific authentication methods.
  'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_URL = 'twitter_login'
LOGIN_REDIRECT_URL = 'main'

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'staticfiles')

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


DICPICK_ENV = os.environ.get('DICPICK_ENV', 'dicpick_dev')

if DICPICK_ENV == 'dicpick_dev':
  from main.settings_dev import *
elif DICPICK_ENV == 'dicpick_prod':
  from main.settings_prod import *

INTERNAL_IPS = [
  '127.0.0.1'
]

template_loaders = (
  # Note that order matters: We want our allauth templates to override the allauth app's defaults,
  # so we must try the filesystem loader before looking in any app dirs.
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  'admin_tools.template_loaders.Loader',
)

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
      # Overrides of templates loaded by other apps, such as allauth.
      # These paths should use forward slashes even on Windows.
      '{}/dicpick/templates'.format(SITE_ROOT)
    ],
    'OPTIONS': {
    'context_processors': [
      'django.template.context_processors.debug',
      'django.template.context_processors.request',
      'django.contrib.auth.context_processors.auth',
      'django.contrib.messages.context_processors.messages',
    ],
    'loaders': maybe_cache_templates(template_loaders),
    'debug': DEBUG,
    },
  },
]

MATERIALITY_DJANGO_STATIC_IGNORE_FILE = 'main/ignore_patterns.txt'
