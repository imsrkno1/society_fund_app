# members/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Login view as the homepage
    path('', views.login_view, name='login'),
    # Registration page
    path('register/', views.register_view, name='register'),
    # Logout view
    path('logout/', views.logout_view, name='logout'),
    # The main index page for logged-in users
    path('index/', views.index_view, name='index'),
]
