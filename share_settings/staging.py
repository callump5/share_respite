from share_settings.base import *
import dj_database_url

DEBUG = False




DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}




# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

HOST_SCHEME                     = "https://"
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True