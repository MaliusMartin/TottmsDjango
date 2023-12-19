from django.db import models
from locationApp.models import Region, District
from userApp.models import Teacher, EducationOfficer, TamisemiUser, DistrictExecutiveDirector, UtumishiUser, EducationLevel, Course, WorkerGrade, Subject, SchoolLevel, School
from django.db import models
from django.contrib.auth import get_user_model

class TransferReasons(models.Model):
    reason = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return self.reason
    
# userApp/models.py



class Application(models.Model):
    APPLICANT_CHOICES = [
        ('teacher', 'Exchange Transfer Application'),
        ('teacher', 'Direct Transfer Application'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    applicant_type = models.CharField(max_length=10, choices=APPLICANT_CHOICES)
    reason = models.TextField()
    supporting_document = models.FileField(upload_to='supporting_documents/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    # Fields specific to Teacher Application
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    grade = models.ForeignKey(WorkerGrade, on_delete=models.CASCADE, null=True)
    subjects_taught = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    school_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)

    # Fields specific to Transfer Application
    region_from = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='transfer_application_region_from', null=True)
    district_from = models.ForeignKey(District, on_delete=models.CASCADE, related_name='transfer_application_district_from', null=True)
    region_to = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='transfer_application_region_to', null=True)
    district_to = models.ForeignKey(District, on_delete=models.CASCADE, related_name='transfer_application_district_to', null=True)
    is_confirmed = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_applicant_type_display()} Application - {self.user.username} - {self.submitted_at}"

    


class TransferVerification(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    verified_officer = models.ForeignKey(EducationOfficer, on_delete=models.CASCADE)
    verified_ded = models.ForeignKey(DistrictExecutiveDirector, on_delete=models.CASCADE)
    verification_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

class TransferSubmission(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(EducationOfficer, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)

class TamisemiConfirmation(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    confirmed_by = models.ForeignKey(TamisemiUser, on_delete=models.CASCADE)
    confirmation_date = models.DateTimeField(auto_now_add=True)

class UtumishiTransfer(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    transferred_by = models.ForeignKey(UtumishiUser, on_delete=models.CASCADE)
    transfer_date = models.DateTimeField(auto_now_add=True)
    salary_transfer_complete = models.BooleanField(default=False)
