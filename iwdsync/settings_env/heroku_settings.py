"""iwdsync/settings_env/heroku_settings.py
"""
import os
import dj_database_url
from decouple import config


DEBUG = False
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALLOWED_HOSTS = ["iwdsync.herokuapp.com"]


DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CACHES = {
    'default': {
        # Use django-bmemcached
        'BACKEND': 'django_bmemcached.memcached.BMemcached',

        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': 60,

        'LOCATION': config('MEMCACHIER_SERVERS'),

        'OPTIONS': {
            'username': config('MEMCACHIER_USERNAME'),
            'password': config('MEMCACHIER_PASSWORD'),
        }
    }
}

CORS_ORIGIN_WHITELIST = [
    "https://iwdsync.vercel.app",
    "https://iwdsync.antigravity.vercel.app",
]
CSRF_TRUSTED_ORIGINS = ["iwdsync.vercel.app", "iwdsync.antigravity.vercel.app"]
CORS_ALLOW_CREDENTIALS = True
