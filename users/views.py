from django.shortcuts import render,redirect
from .models import CustomUser
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ChangePasswordView(CreateView):
    form_class = CustomUserChangeForm
    template_name = './auth/password_change_form.html'
    queryset = CustomUser.objects.all()

