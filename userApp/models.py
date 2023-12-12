from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MinLengthValidator
from locationApp.models import SchoolLevel, Region, District, School

class Course(models.Model):
    name = models.CharField(max_length=100)
    coursecode=models.IntegerField( unique=True,null=True)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    subjectcode=models.IntegerField( unique=True,null=True)

    def __str__(self):
        return self.name
    
# the WorkerGrade model
    
class WorkerGrade(models.Model):
    grade = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.grade

# the SalaryScale model
    
class SalaryScale(models.Model):
    scale= models.CharField(max_length=50,null=True)
    amount = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.scale

#the gender model

class Gender(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class KindOfOfficer(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

#the position model
    
class Position(models.Model):
    name = models.CharField(max_length=110)
    def __str__(self) -> str:
        return self.name


class EducationLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    # Add any additional user fields here, if needed
    
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, )
    phone = models.CharField(max_length=100)
    birthdate = models.DateTimeField(null=True)
    nin = models.CharField(max_length=20, null=True, blank=True,
    validators=[
        MaxLengthValidator(limit_value=20),
        MinLengthValidator(limit_value=20),
    ])
    image = models.ImageField(max_length=255, upload_to='images/', null=True, blank=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE, null=True)
    is_teacher = models.BooleanField(default=False)
    is_education_officer = models.BooleanField(default=False)
    is_ded = models.BooleanField(default=False)
    is_tamisemi = models.BooleanField(default=False)
    is_utumishi = models.BooleanField(default=False)
    password = models.CharField(max_length=180, null=True, blank=True)  # You should hash and salt passwords
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('bcrypt_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    created_at = models.DateTimeField(auto_now_add=True)
    retirement = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    
    
    def save(self, *args, **kwargs):
        if self.birthdate and self.created_at:
            # Calculate the expected retirement date
            years_of_service = (self.created_at - self.birthdate).days / 365
            retirement_age = 60  
            retirement_date = self.birthdate + timezone.timedelta(days=int((retirement_age - years_of_service) * 365))
        
            self.retirement = retirement_date

        super(CustomUser, self).save(*args, **kwargs)

def __str__(self):
    return f"{self.lname} - {self.fname} {self.username}"

    
    pass

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    grade = models.ForeignKey(WorkerGrade, on_delete=models.CASCADE, null=True)
    subjects_taught = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    school_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.user},{self.school_level},{self.region} {self.district}"
    # Add teacher-specific fields here

class EducationOfficer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    type = models.ForeignKey(KindOfOfficer, on_delete=models.CASCADE,null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    # Add education officer-specific fields here
    
class DistrictExecutiveDirector(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    
class TamisemiUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add Tamisemi-specific fields here

class UtumishiUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add Utumishi-specific fields here

