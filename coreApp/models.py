from django.db import models

# Create your models here.
# dashboard/models.py
from django.db import models
from userApp.models import Teacher, EducationOfficer, TamisemiUser, DistrictExecutiveDirector, UtumishiUser

class DashboardItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

class TransferApplicationStatus(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=255)  # Example field, replace with actual details
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add other fields as needed
