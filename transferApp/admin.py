from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TransferReasons, Application, TransferVerification, TransferSubmission, TamisemiConfirmation, TransferVerification, TransferSubmission,  TamisemiConfirmation,UtumishiTransfer

# Register your models here.

class TransferReasonAdmin(admin.ModelAdmin):
    list_display = ('reason', )
    search_fields = ('reason', ) 
    
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'applicant_type', 'reason', 'submitted_at', 'is_confirmed', 'is_verified')
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname', 'applicant_type', 'reason', 'is_confirmed', 'is_verified')
    list_filter = ('applicant_type', 'is_confirmed', 'is_verified')
    
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'applicant_type', 'reason', 'submitted_at', 'is_confirmed', 'is_verified')
    search_fields = ('user__username', 'user__email', 'user__fname', 'user__lname', 'applicant_type', 'reason', 'is_confirmed', 'is_verified')
    list_filter = ('applicant_type', 'is_confirmed', 'is_verified')
    
class TransferVerificationAdmin(admin.ModelAdmin):
    list_display = ('application', 'verified_officer', 'verified_ded', 'verification_date', 'is_verified')
    search_fields = ('application__user__username', 'application__user__email', 'application__user__fname', 'application__user__lname', 'verified_officer__user__username', 'verified_officer__user__email', 'verified_officer__user__fname', 'verified_officer__user__lname', 'verified_ded__user__username', 'verified_ded__user__email', 'verified_ded__user__fname', 'verified_ded__user__lname', 'is_verified')
    list_filter = ('is_verified',)  
    
class TransferSubmissionAdmin(admin.ModelAdmin):
    list_display = ('application', 'submitted_by', 'submission_date')
    search_fields = ('application__user__username', 'application__user__email', 'application__user__fname', 'application__user__lname', 'submitted_by__user__username', 'submitted_by__user__email', 'submitted_by__user__fname', 'submitted_by__user__lname')
    list_filter = ('submission_date',)
    
class TamisemiConfirmationAdmin(admin.ModelAdmin):
    list_display = ('application', 'confirmed_by', 'confirmation_date')
    search_fields = ('application__user__username', 'application__user__email', 'application__user__fname', 'application__user__lname', 'confirmed_by__user__username', 'confirmed_by__user__email', 'confirmed_by__user__fname', 'confirmed_by__user__lname')
    list_filter = ('confirmation_date',)
    
class UtumishiTransferAdmin(admin.ModelAdmin):
    list_display = ('application',  'transfer_date')
    search_fields = ('application__user__username', 'application__user__email', 'application__user__fname', 'application__user__lname', 'transfered_by__user__username', 'transfered_by__user__email', 'transfered_by__user__fname', 'transfered_by__user__lname')
    list_filter = ('transfer_date',)
    
    
admin.site.register(TransferReasons, TransferReasonAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(TransferVerification, TransferVerificationAdmin)
admin.site.register(TransferSubmission, TransferSubmissionAdmin)
admin.site.register(TamisemiConfirmation, TamisemiConfirmationAdmin)
admin.site.register(UtumishiTransfer, UtumishiTransferAdmin)
admin.site.site_header = "TOTTMS ADMIN"