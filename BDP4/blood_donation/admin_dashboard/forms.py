from django import forms
from .models import User
from .models import AdminBloodRequest

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User  # Should be the model class, not a string
        fields = ['email', 'username', 'is_active', 'is_staff', 'is_admin']

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = AdminBloodRequest
        fields = ['blood_type', 'amount_needed', 'request_status']
