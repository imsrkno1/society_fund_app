# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # The root URL path ('') now points to your login_view.
    path('', views.login_view, name='login'),
    
    # This path is for the page a user sees after logging in.
    path('index/', views.index_view, name='index'),
]
