# mysociety/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The default Django admin path
    path('admin/', admin.site.urls),

    # This line tells Django to look inside your 'members' app for more URL patterns
    # The empty string '' means that any incoming URL will first be checked against
    # the patterns defined in members/urls.py.
    path('', include('members.urls')),
]
