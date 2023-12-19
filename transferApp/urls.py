# userApp/urls.py
from django.urls import path
from .views import teacher_application_view, get_districts

urlpatterns = [
    # Your existing URLs...
    path('application/', teacher_application_view, name='teacher_application'),
    # Add this to your Django urls.py
    path('get-districts/', get_districts, name='get_districts'),

]
