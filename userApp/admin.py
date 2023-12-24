from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Teacher, EducationOfficer, DistrictExecutiveDirector, TamisemiUser, UtumishiUser,Course


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'fname', 'mname', 'lname', 'gender', 'phone', 'birthdate', 'nin', 'position', 'is_teacher', 'is_education_officer', 'is_ded', 'is_tamisemi', 'is_utumishi', 'created_at', 'retirement', 'updated_at',)
    search_fields = ('username', 'email', 'fname', 'lname')
    list_filter = ('is_teacher', 'is_education_officer', 'is_ded', 'is_tamisemi', 'is_utumishi', 'position')

# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('user', 'education_level', 'grade', 'subjects_taught', 'region', 'district', 'school_level', 'school','course')
#     search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname','subjects_taught','course')
#     list_filter = ('education_level', 'grade', 'region', 'district', 'school_level', 'school','subjects_taught', 'course')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'education_level', 'course', 'grade', 'display_subjects', 'region', 'district', 'school_level', 'school')
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname','display_subjects','course')
    list_filter = ('education_level', 'grade', 'region', 'district', 'school_level', 'school', 'course')

    def display_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects_taught.all()])
    
    display_subjects.short_description = 'Subjects Taught'  # Set a custom column header for the subjects


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

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'coursecode')
    search_fields = ('name', 'coursecode')
    list_filter = ('name', 'coursecode')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(EducationOfficer, EducationOfficerAdmin)
admin.site.register(DistrictExecutiveDirector, DistrictExecutiveDirectorAdmin)
admin.site.register(TamisemiUser, TamisemiUserAdmin)
admin.site.register(UtumishiUser, UtumishiUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.site_header = "TOTTMS ADMIN"
