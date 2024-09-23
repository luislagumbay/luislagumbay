from django.urls import path
from .views import BloodRequestCreateView, BloodRequestListView, BloodRequestDetailView, BloodRequestUpdateView, BloodRequestDeleteView, admin_dashboard, admin_user_edit, admin_user_delete, admin_blood_request_edit, admin_blood_request_delete

urlpatterns = [
    path('create/', BloodRequestCreateView.as_view(), name='blood_request_create'),
    path('', BloodRequestListView.as_view(), name='blood_request_list'),
    path('<int:pk>/', BloodRequestDetailView.as_view(), name='blood_request_detail'),
    path('<int:pk>/edit/', BloodRequestUpdateView.as_view(), name='blood_request_edit'),
    path('<int:pk>/delete/', BloodRequestDeleteView.as_view(), name='blood_request_delete'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-user/<int:pk>/edit/', admin_user_edit, name='admin_user_edit'),
    path('admin-user/<int:pk>/delete/', admin_user_delete, name='admin_user_delete'),
    path('admin-blood-request/<int:pk>/edit/', admin_blood_request_edit, name='admin_blood_request_edit'),
    path('admin-blood-request/<int:pk>/delete/', admin_blood_request_delete, name='admin_blood_request_delete'),
]
