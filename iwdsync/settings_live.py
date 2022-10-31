from iwdsync.settings import *
import os
import dj_database_url

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


DEBUG = False
ALLOWED_HOSTS = ["iwdsync.fly.dev"]


DATABASES = {}
DATABASES["default"] = dj_database_url.parse(os.environ.get('DATABASE_URL', 'sqlite:///fake.db'), conn_max_age=600)


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
CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SAMESITE = "None"

CORS_ORIGIN_WHITELIST = [
    "https://iwdsync.vercel.app",
    "https://iwdsync-git-master.import-antigravity.vercel.app",
    "https://iwdsync.import-antigravity.vercel.app",
    "https://iwdlive.com",
    "https://dev.iwdlive.com",
]

CSRF_TRUSTED_ORIGINS = [
    "iwdsync.vercel.app",
    "iwdsync-git-master.import-antigravity.vercel.app",
    "iwdsync.import-antigravity.vercel.app",
    "iwdsync.app",
    "iwdlive.com",
    "dev.iwdlive.com",
    "iwdsync.fly.dev",
]
CORS_ALLOW_CREDENTIALS = True

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN", ""),
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
