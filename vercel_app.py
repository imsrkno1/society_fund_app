# vercel_app.py
import os
import sys

# Add the project root to the system path.
# This ensures that when Vercel runs this file, it can find
# your `mysociety` module and all other project files.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())
sys.path.insert(1, os.path.join(os.getcwd(), 'mysociety'))


# Set the Django settings module explicitly.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysociety.settings')

# This is a standard practice to handle Vercel's specific
# environment and ensure Django is ready to serve.
try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except ImportError:
    # Handle the case where Django is not found, which could be
    # due to a build issue or environment problem.
    raise ImportError(
        "Could not import Django. Ensure your requirements.txt is correct "
        "and that the project structure is valid."
    )

# Vercel's Python runtime requires a top-level variable named `app`.
# We assign our Django `application` to it.
app = application
