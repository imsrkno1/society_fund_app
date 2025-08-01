# mysociety/urls.py

"""
URL configuration for mysociety project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from members import views as members_views # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', members_views.home, name='home'),
    path('login/', members_views.user_login, name='login'),
    path('register/', members_views.register, name='register'),
    path('dashboard/', members_views.dashboard, name='dashboard'),
    path('logout/', members_views.user_logout, name='logout'),
    path('add_transaction/', members_views.add_transaction, name='add_transaction'),
    path('pay_dues/', members_views.pay_dues, name='pay_dues'),
    path('transactions/', members_views.transaction_list, name='transaction_list'),
    path('members/', members_views.member_list, name='member_list'), # New URL for member list
    path('api/get_user_details/<str:house_no>/', members_views.get_user_details_api, name='get_user_details_api'),
]

urlpatterns = [
    # The root URL path ('') now points to your login_view.
    # We give it the name 'login' for easy reference.
    path('', views.login_view, name='login'),
    
    # This path is for the page a user sees after logging in.
    # The name 'index' matches the redirect in your views.py.
    path('index/', views.index_view, name='index'),
]
