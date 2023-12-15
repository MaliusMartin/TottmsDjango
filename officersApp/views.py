# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from .models import SomeModel  # Import other models if needed
# from .forms import AddTeacherForm



# class AddTeacherView(CreateView):
#     model = SomeModel  # Use the appropriate model
#     form_class = AddTeacherForm
#     template_name = 'officersApp/addteacher.html'  # Create this template next
#     success_url = '/success/'  # Redirect to a success page after form submission
# officersApp/views.py

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import AddTeacherForm
from django.urls import reverse_lazy
from .models import Teacher

class AddTeacherView(CreateView):
    model = Teacher
    form_class = AddTeacherForm
    template_name = 'officersApp/addteacher.html'
    success_url = reverse_lazy('officersApp:add_teacher')
