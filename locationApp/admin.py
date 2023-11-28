from django.contrib import admin
from .models import SchoolLevel, Region, District, School

class SchoolLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'levelName', 'subvote')
    search_fields = ('levelName',)
    list_filter = ('subvote',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ()

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'votecode', 'region')
    search_fields = ('name', 'votecode')
    list_filter = ('region',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district', 'region', 'School_level')
    search_fields = ('name',)
    list_filter = ('district', 'region', 'School_level')

admin.site.register(SchoolLevel, SchoolLevelAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(School, SchoolAdmin)
