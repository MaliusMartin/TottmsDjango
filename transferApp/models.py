from django.db import models
from locationApp.models import Region, District
from userApp.models import Teacher, EducationOfficer, TamisemiUser, DistrictExecutiveDirector, UtumishiUser

class TransferReasons(models.Model):
    reason = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return self.reason
    
class TransferApplication(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    region_from = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='transfer_application_region_from')
    district_from = models.ForeignKey(District, on_delete=models.CASCADE, related_name='transfer_application_district_from')
    region_to = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='transfer_application_region_to')
    district_to = models.ForeignKey(District, on_delete=models.CASCADE, related_name='transfer_application_district_to')
    reason = models.ForeignKey(TransferReasons, on_delete=models.CASCADE, null=True )
    application_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

class SupportingDocument(models.Model):
    application = models.ForeignKey(TransferApplication, on_delete=models.CASCADE)
    document = models.FileField(upload_to='supporting_documents/')
    # Add other fields as needed, such as a description, date uploaded, etc.

class TransferVerification(models.Model):
    application = models.ForeignKey(TransferApplication, on_delete=models.CASCADE)
    verified_officer = models.ForeignKey(EducationOfficer, on_delete=models.CASCADE)
    verified_ded = models.ForeignKey(DistrictExecutiveDirector, on_delete=models.CASCADE)
    verification_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

class TransferSubmission(models.Model):
    application = models.OneToOneField(TransferApplication, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(EducationOfficer, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)

class TamisemiConfirmation(models.Model):
    application = models.OneToOneField(TransferApplication, on_delete=models.CASCADE)
    confirmed_by = models.ForeignKey(TamisemiUser, on_delete=models.CASCADE)
    confirmation_date = models.DateTimeField(auto_now_add=True)

class UtumishiTransfer(models.Model):
    application = models.OneToOneField(TransferApplication, on_delete=models.CASCADE)
    transferred_by = models.ForeignKey(UtumishiUser, on_delete=models.CASCADE)
    transfer_date = models.DateTimeField(auto_now_add=True)
    salary_transfer_complete = models.BooleanField(default=False)
