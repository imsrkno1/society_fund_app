"""
WSGI config for mysociety project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Add the project's root directory to the Python path
# This is a robust way to ensure all modules are found.
path = os.path.expanduser('/opt/render/project/src')
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysociety.settings')

application = get_wsgi_application()

# This is the crucial line for Vercel. We need to expose the application
# under the name `app` as well, as this is what Vercel's Python runtime expects.
app = application
