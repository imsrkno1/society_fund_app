# mysociety/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the members app's URLs at the root of the site
    path('', include('members.urls')),
]
