# from django.urls import path, include


# from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# from django.urls import path

# app_name = 'userApp'
# urlpatterns = [
#     # ... other URL patterns ...
#     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
#     # ... other URL patterns ...
#       # ... other URL patterns ...
#     path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
#     path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
#     path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
#     # ... other URL patterns ...
# ]
from django.urls import path
from .views import CustomLoginView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from .views import CustomSignupView, CustomPasswordResetConfirmView, Teachers_list, profile_view 


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile_view, name='user_profile'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('teachers/', Teachers_list, name='teachers'),
    # path('teachers/<int:teacher_id>/', Teachers_list, name='teachers'),
    
    
]
