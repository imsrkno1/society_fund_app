# mysociety/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # This is your admin page.
    path('admin/', admin.site.urls),

    # This line tells Django to look inside the members app for URLs.
    # The empty string '' means it will match from the root of your domain.
    path('', include('members.urls')),
]
