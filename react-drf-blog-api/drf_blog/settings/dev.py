from .base import *

DEBUG = False

ALLOWED_HOSTS += [
    env("BACKEND_DOMAIN"),
]


DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}


REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%b %d, %Y",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}
