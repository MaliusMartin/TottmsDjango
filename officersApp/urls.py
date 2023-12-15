from django.urls import path, include


# from . import views
from .views import AddTeacherView

app_name = 'officersApp'

urlpatterns = [
    
    # path('officers/', views.officers, name='officers'),
    # path('officers/<int:officer_id>/', views.officer, name='officer'),
    # path('officers/add/', views.add_officer, name='add_officer'),
    path('addteacher/', AddTeacherView.as_view(), name='add_teacher'),
    
]
