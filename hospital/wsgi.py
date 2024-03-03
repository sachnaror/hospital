
from django.core.management import execute_from_command_line
import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')

application = get_wsgi_application()


execute_from_command_line(sys.argv)
