import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsc2000.settings.zhaoqin")

application = get_wsgi_application()
