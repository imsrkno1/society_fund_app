from django.urls import path
from . import views

# This list defines the URL patterns for your application.
urlpatterns = [
    # The login page is at the URL path "login/".
    # It calls the 'login_view' function from your views.
    path('login/', views.login_view, name='login'),
    
    # The index page is at the root URL path "".
    # It calls the 'index_view' function from your views.
    path('', views.index_view, name='index'),
]
