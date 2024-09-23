# blood/forms.py

from django import forms
from .models import BloodRequest

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality']
