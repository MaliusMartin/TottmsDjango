# transferApp/forms.py
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['region_from', 'district_from', 'region_to', 'district_to',  'reason', 'supporting_document']
