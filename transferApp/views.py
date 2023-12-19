
from django.shortcuts import render, redirect
from .forms import ApplicationForm
from django.http import JsonResponse
from locationApp.models import District

def teacher_application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and do any additional processing
            form.save()
            return redirect('application_success')  # Redirect to a success page
    else:
        form = ApplicationForm()

    return render(request, 'transferApp/transferApplication.html', {'form': form})


def get_districts(request):
    region_id = request.GET.get('region_id')
    # Perform a query to get the districts based on the region_id
    districts = District.objects.filter(region_id=region_id).values('id', 'name')
    return JsonResponse({'districts': list(districts)})
