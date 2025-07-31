# vercel-build.sh
# This script explicitly tells Vercel how to set up and build your Django project.

# Exit immediately if a command exits with a non-zero status.
set -o errexit

# Install all Python dependencies listed in requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations to ensure the database schema is up-to-date
echo "Running database migrations..."
python mysociety/manage.py migrate

# Collect static files for the Django admin and your app
echo "Collecting static files..."
python mysociety/manage.py collectstatic --no-input

echo "Build process complete."
