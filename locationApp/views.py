from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import School, SchoolLevel, Region, District
# from userApp.models import Supervisor

def school_list_view(request):
    # Get the selected school level from the query parameters
    selected_school_level = request.GET.get('school_level')

    # Get all school levels for dropdown
    all_school_levels = SchoolLevel.objects.all()

    # Get all schools or filter by selected school level
    if selected_school_level:
        schools = School.objects.filter(School_level__levelName=selected_school_level)
    else:
        schools = School.objects.all()

    # Count total schools, primary schools, and secondary schools
    total_schools_count = School.objects.count()
    primary_schools_count = School.objects.filter(School_level__levelName='Primary').count()
    secondary_schools_count = School.objects.filter(School_level__levelName='Secondary').count()

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(schools, 10)  # Show 10 schools per page
    try:
        schools = paginator.page(page)
    except PageNotAnInteger:
        schools = paginator.page(1)
    except EmptyPage:
        schools = paginator.page(paginator.num_pages)

    return render(request, 'locationApp/schools.html', {
        'schools': schools,
        'all_school_levels': all_school_levels,
        'selected_school_level': selected_school_level,
        'total_schools_count': total_schools_count,
        'primary_schools_count': primary_schools_count,
        'secondary_schools_count': secondary_schools_count,
    })



def region_list(request):
    regions = Region.objects.all()
    return render(request, 'locationApp/region.html', {'regions': regions})