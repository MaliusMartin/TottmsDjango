from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
# userApp/views.py
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from .forms import SignupForm
from datetime import datetime
# from django.contrib.auth.decorators import login_required



class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    # redirect_authenticated_user = True

    def form_valid(self, form):
        # Call the parent class's form_valid method to perform the default login actions
        response = super().form_valid(form)

        # Customize the redirection based on the user's group
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='Teachers').exists():
                # Redirect teachers to the teacher profile URL
                return redirect('user_profile')
            elif user.groups.filter(name='Educationofficers').exists():
                # Redirect Education officers to the Education officer profile URL
                return redirect('user_profile')
            elif user.groups.filter(name='Districtofficers').exists():
                # Redirect District officers to the District officer profile URL
                return redirect('user_profile')
            elif user.groups.filter(name='Tamisemi').exists():
                # Redirect Tamisemi users to the Tamisemi profile URL
                return redirect('tamisemi_profile')
            elif user.groups.filter(name='Utumishi').exists():
                # Redirect Utumishi users to the Utumishi profile URL
                return redirect('user_profile')
            else:
                # Redirect to the default profile URL
                return redirect('user_profile')

        return response

 
# views.py



# @login_required
def profile_view(request):
    user = request.user
    is_teacher = user.groups.filter(name='Teachers').exists()
    is_education_officer = user.groups.filter(name='Educationofficers').exists()
    is_district_officer = user.groups.filter(name='Districtofficers').exists()
    is_tamisemi = user.groups.filter(name='Tamisemi').exists()
    is_utumishi = user.groups.filter(name='Utumishi').exists()
    
    current_time = datetime.now().time()

    # Determine the time of day
    if current_time.hour < 12:
        greeting = "Good morning"
    elif 12 <= current_time.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    context = {
        'greeting': f'{greeting}, {request.user.username}',
        'user': user,
        'is_teacher': is_teacher,
        'is_education_officer': is_education_officer,
        'is_district_officer': is_district_officer,
        'is_tamisemi': is_tamisemi,
        'is_utumishi': is_utumishi,
    }

    return render(request, 'userApp/profile.html', context)

# Password reset views
class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
    

User = get_user_model()

class CustomPasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    success_url = '/user/login/'
    template_name = 'userApp/signup_confirm.html'

    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            return User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return None

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        user = self.get_user(uidb64)
        if user is None or not default_token_generator.check_token(user, kwargs['token']):
            return self.render_to_response(self.get_context_data())
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        uidb64 = self.kwargs['uidb64']
        user = self.get_user(uidb64)
        if user is not None and default_token_generator.check_token(user, self.kwargs['token']):
            form.save()
            return super().form_valid(form)
        return self.form_invalid(form)

class CustomSignupView(FormView):
    template_name = 'userApp/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        check_number = form.cleaned_data['check_number']
        user = get_object_or_404(User, username=check_number)
        return render(self.request, 'userApp/signup_confirm.html', {'user': user})

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


# Other views...

