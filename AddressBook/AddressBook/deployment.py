import os 
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['addressbookdjango.azurewebsites.net']]
# CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['addressbookdjango.azurewebsites.net']]
CSRF_TRUSTED_ORIGINS = ['https://addressbookdjango.azurewebsites.net']
DEBUG = False


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')