# Local settings for Django projects
# Set all values here before starting the project
# Move this file to the same folder as main settings.py file
# Rename the file as local_settings.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Disable DEBUG in a deployment server
DEBUG = True

# Enable SESSION_COOKIE_SECURE while using SSL
SESSION_COOKIE_SECURE = False

ADMINS = (
    ('Titli Sarkar', 'titli010203@gmail.com'),
    ('Seshagiri Prabhu', 'seshagiriprabhu@gmail.com'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DATETIME_FORMAT = ('d-m-Y H:i')


# If running in debug mode, write emails to files.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts

#ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }



# Cache backend.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}
