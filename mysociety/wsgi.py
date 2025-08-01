"""
WSGI config for mysociety project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# This section is critical for Vercel. We need to explicitly set up the
# Python path so the runtime can find our project modules.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
    
# Now, we need to add the parent directory of our project to the path
# for example, if 'mysociety' is in 'project_root', we need to add 'project_root'
# The `os.getcwd()` method is a good way to get the current working directory,
# which for Vercel is the root of your project.
if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())


from django.core.wsgi import get_wsgi_application

# We are setting the Django settings module explicitly.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysociety.settings')

application = get_wsgi_application()

# This is the variable Vercel expects to find. We are assigning the
# Django application to a variable named `app`.
app = application
