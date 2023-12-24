from django.urls import path, include



from .views import school_list_view, region_list

app_name = 'locationApp'
# urls.py

urlpatterns = [
    path('schools/', school_list_view, name='schools'),
    path('regions/', region_list, name='regions'),
]
