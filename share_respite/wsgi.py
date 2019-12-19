"""
WSGI config for share_respite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.conf.global_settings import DEBUG
from django.core.wsgi import get_wsgi_application

if DEBUG == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_settings.staging')


application = get_wsgi_application()
