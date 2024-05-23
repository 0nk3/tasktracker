import os

from django.core.wsgi import get_wsgi_application

# Set environment variable (if needed for your project)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasktracker.settings')

# Get the WSGI application object
application = get_wsgi_application()