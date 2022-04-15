"""iwdsync/settings_env/heroku_settings.py
"""
import os
import dj_database_url
from decouple import config

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


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
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'iwd-cache',
    }
}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CORS_ORIGIN_WHITELIST = [
    "https://iwdsync.vercel.app",
    # "https://iwdsync.antigravity.vercel.app",
    # "https://iwdsync-git-master.antigravity.vercel.app",
    "https://iwdsync-git-master.import-antigravity.vercel.app",
    "https://iwdsync.import-antigravity.vercel.app",
    "https://iwdsync.app",
    "https://iwdlive.com",
    "https://costream.me",
]

CSRF_TRUSTED_ORIGINS = [
    "iwdsync.herokuapp.com",
    "iwdsync.vercel.app",
    # "iwdsync.antigravity.vercel.app",
    # "iwdsync-git-master.antigravity.vercel.app",
    "iwdsync-git-master.import-antigravity.vercel.app",
    "iwdsync.import-antigravity.vercel.app",
    "iwdsync.app",
    "iwdlive.com",
    "costream.me",
]
CORS_ALLOW_CREDENTIALS = True

sentry_sdk.init(
    dsn=config("SENTRY_DSN", ""),
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
