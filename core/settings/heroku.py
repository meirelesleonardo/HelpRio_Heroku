import environ
from core.settings.base import *


env = environ.Env()
DEBUG = env.bool("DEBUG", False)
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DATABASES = {
    "default": env.db(),
}