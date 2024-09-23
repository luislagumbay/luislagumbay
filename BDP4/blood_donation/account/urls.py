# account/urls.py
from django.urls import path
from .views import register, login_user, profile_view, update_profile, create_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', profile_view, name='profile_view'),
    path('profile/update/', update_profile, name='update_profile'),
    path('create_profile/', create_profile, name='create_profile'),

]
