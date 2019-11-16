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


#AWS
AWS_ACCESS_KEY_ID = str(os.getenv("AWS_ACCESS_KEY_ID"))
AWS_SECRET_ACCESS_KEY = str(os.getenv("AWS_SECRET_ACCESS_KEY"))

#reCaptch
GOOGLE_RECAPTCHA_SECRET_KEY = str(os.getenv("GOOGLE_RECAPTCHA_SECRET_KEY"))

#Email
EMAIL_HOST_USER = str(os.getenv("EMAIL_HOST_USER"))
EMAIL_HOST_PASSWORD = str(os.getenv("EMAIL_HOST_PASSWORD"))

# STRIPE
STRIPE_SECRET_KEY = str(os.getenv("STRIPE_SECRET_KEY"))
STRIPE_PUBLISHABLE_KEY = str(os.getenv("STRIPE_PUBLISHABLE_KEY"))
stripe.api_key = str(os.getenv("STRIPE_SECRET_KEY"))