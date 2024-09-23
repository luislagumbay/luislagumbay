# admin_dashboard/urls.py
from django.urls import path
from .views import admin_dashboard, admin_user_edit, admin_user_delete, admin_blood_request_edit, admin_blood_request_delete

urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('user/edit/<int:pk>/', admin_user_edit, name='admin_user_edit'),
    path('user/delete/<int:pk>/', admin_user_delete, name='admin_user_delete'),
    path('blood_request/edit/<int:pk>/', admin_blood_request_edit, name='admin_blood_request_edit'),
    path('blood_request/delete/<int:pk>/', admin_blood_request_delete, name='admin_blood_request_delete'),
]
