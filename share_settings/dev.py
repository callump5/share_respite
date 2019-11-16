from share_settings.base import *
from aws import AWS_SECRET_ACCESS_KEY as AWS_KEY
from aws import AWS_ACCESS_KEY_ID as AWS_ID,  EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, GOOGLE_RECAPTCHA_SECRET_KEY

EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD

AWS_ACCESS_KEY_ID = AWS_ID
AWS_SECRET_ACCESS_KEY = AWS_KEY

GOOGLE_RECAPTCHA_SECRET_KEY = GOOGLE_RECAPTCHA_SECRET_KEY


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

