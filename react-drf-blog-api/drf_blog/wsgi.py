import os

from django.core.wsgi import get_wsgi_application
from drf_blog.settings.base import env

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"drf_blog.settings.{env('ENV_MODE')}")

application = get_wsgi_application()
