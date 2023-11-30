from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Teacher, EducationOfficer, DistrictExecutiveDirector, TamisemiUser, UtumishiUser


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'fname', 'mname', 'lname', 'gender', 'phone', 'birthdate', 'nin', 'position', 'is_teacher', 'is_education_officer', 'is_ded', 'is_tamisemi', 'is_utumishi', 'created_at', 'retirement', 'updated_at')
    search_fields = ('username', 'email', 'fname', 'lname')
    list_filter = ('is_teacher', 'is_education_officer', 'is_ded', 'is_tamisemi', 'is_utumishi', 'position')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'education_level', 'grade', 'subjects_taught', 'region', 'district', 'school_level', 'school')
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname','subjects_taught')
    list_filter = ('education_level', 'grade', 'region', 'district', 'school_level', 'school','subjects_taught')

class EducationOfficerAdmin(admin.ModelAdmin):
    list_display = ('user', 'region', 'district')
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname')
    list_filter = ('region', 'district')

class DistrictExecutiveDirectorAdmin(admin.ModelAdmin):
    list_display = ('user', 'region', 'district')
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname')
    list_filter = ('region', 'district')

class TamisemiUserAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname')

class UtumishiUserAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(EducationOfficer, EducationOfficerAdmin)
admin.site.register(DistrictExecutiveDirector, DistrictExecutiveDirectorAdmin)
admin.site.register(TamisemiUser, TamisemiUserAdmin)
admin.site.register(UtumishiUser, UtumishiUserAdmin)
admin.site.site_header = "TOTTMS ADMIN"
