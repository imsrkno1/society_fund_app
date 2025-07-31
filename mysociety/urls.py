# society_fund_app/mysociety/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from members import views as members_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', members_views.dashboard_view, name='dashboard'),
    path('login/', members_views.login_view, name='login'),
    path('register/', members_views.register_view, name='register'),
    path('logout/', members_views.logout_view, name='logout'),
    path('members/', members_views.member_list_view, name='member_list'),
    path('pay_dues/', members_views.pay_dues_view, name='pay_dues'),
    path('add_transaction/', members_views.add_transaction_view, name='add_transaction'),
    path('transactions/', members_views.transaction_list_view, name='transaction_list'),
    path('api/get_user_details/<str:house_no>/', members_views.get_user_details_api, name='get_user_details_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
