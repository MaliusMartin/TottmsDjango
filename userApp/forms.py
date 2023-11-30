# userApp/forms.py
from django import forms

class SignupForm(forms.Form):
    check_number = forms.CharField(max_length=100, label='Check Number')
