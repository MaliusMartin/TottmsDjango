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

from .forms import SignupForm
# Your other imports...

# Login view

class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    # redirect_authenticated_user = True
    

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

