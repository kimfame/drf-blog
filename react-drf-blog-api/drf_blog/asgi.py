import os

from django.core.asgi import get_asgi_application
from drf_blog.settings.base import env

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"drf_blog.settings.{env('ENV_MODE')}")

application = get_asgi_application()
