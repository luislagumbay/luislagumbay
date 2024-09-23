from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name', 'weight', 'height', 'region',
            'province', 'municipality', 'blood_type', 'availability', 'last_donation_date']
