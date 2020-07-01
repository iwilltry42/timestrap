from .base import *  # noqa: F401,F403
import os


DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ["SECRET_KEY"]  # noqa: F405


# SECURITY WARNING: set this to your domain name in production!

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "postgres"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "db"),
        "PORT": int(os.environ.get("POSTGRES_PORT", "5432")),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
    }
}


# Channels
# https://channels.readthedocs.io/en/latest/

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (os.environ.get("REDIS_HOST", "redis"), int(os.environ.get("REDIS_PORT", "6379")))
            ]
        },
    }
}


# Email

if os.environ.get("EMAIL_HOST"):  # noqa: E501,F405
    EMAIL_HOST = os.environ.get("EMAIL_HOST")  # noqa: F405
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")  # noqa: F405
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")  # noqa: F405
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 25))  # noqa: F405
    EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS", False))  # noqa: F405
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    EMAIL_ENABLED = False
