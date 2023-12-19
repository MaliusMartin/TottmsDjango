# education_officers/models.py
from django.db import models
from userApp.models import EducationOfficer, DistrictExecutiveDirector,CustomUser, Teacher
from transferApp.models import Application, TransferVerification, TransferSubmission
from locationApp.models import Region, District

class PrimaryEducationOfficer(models.Model):
    education_officer = models.OneToOneField(EducationOfficer, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    # Add other fields specific to primary education officers as needed

class SecondaryEducationOfficer(models.Model):
    education_officer = models.OneToOneField(EducationOfficer, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    # Add other fields specific to secondary education officers as needed
    

class DED(models.Model):
    user = models.OneToOneField('userApp.CustomUser', on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='district_executive_directors_region')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_executive_directors_district')

    # Add other fields as needed

    def __str__(self):
        return f"{self.user}, {self.region}, {self.district}"

class DEDVerification(models.Model):
    ded = models.ForeignKey(DistrictExecutiveDirector, on_delete=models.CASCADE)
    transfer_verification = models.ForeignKey(TransferVerification, on_delete=models.CASCADE)
    verification_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

class DEDSubmission(models.Model):
    ded = models.ForeignKey(DistrictExecutiveDirector, on_delete=models.CASCADE)
    transfer_submission = models.ForeignKey(TransferSubmission, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)

class DEDEducationOfficerTransfer(models.Model):
    ded = models.ForeignKey(DistrictExecutiveDirector, on_delete=models.CASCADE)
    transfer_application = models.ForeignKey(Application, on_delete=models.CASCADE)
    transfer_date = models.DateTimeField(auto_now_add=True)
    is_transferred = models.BooleanField(default=False)

class SomeModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)