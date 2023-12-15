# officersApp/forms.py
from django import forms
from .models import SomeModel  # Import other models if needed

class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = SomeModel  # Use the appropriate model
        fields = '__all__'  # Include all fields or specify the fields you want in the form
