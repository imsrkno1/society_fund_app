# vercel_app.py
import os
import sys

# Add the project's root directory to the Python path
# This ensures Vercel can find your 'mysociety' project folder.
sys.path.insert(0, os.path.dirname(__file__))

# Set the correct Django settings module.
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysociety.settings'

# Import the WSGI application from your Django project.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# This is a common fix for a specific Vercel issue where static files
# are not collected correctly by the build process.
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler

if settings.DEBUG:
    application = StaticFilesHandler(application)
