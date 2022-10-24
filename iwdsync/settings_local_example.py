from iwdsync.settings import *
import os
import dj_database_url


DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALLOWED_HOSTS = ["localhost"]


DATABASES = {}
DATABASES["default"] = dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600, ssl_require=True)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
CSRF_TRUSTED_ORIGINS = ['localhost:3000', 'localhost:8000']
CORS_ALLOW_CREDENTIALS = True

AUTH_PASSWORD_VALIDATORS = []
