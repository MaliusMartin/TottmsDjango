from django.urls import path, include


from . import views

app_name = 'coreApp'
urlpatterns = [
   
    path('', views.index,  name='base'),
  

    
     
]