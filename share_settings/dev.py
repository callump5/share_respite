from share_settings.base import *
from aws import AWS_SECRET_ACCESS_KEY as AWS_KEY
from aws import AWS_ACCESS_KEY_ID as AWS_ID


AWS_ACCESS_KEY_ID = AWS_ID
AWS_SECRET_ACCESS_KEY = AWS_KEY

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
