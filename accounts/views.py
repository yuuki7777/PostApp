from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login
from .models import BaseAccount
from .forms import UserSignUpForm, LoginForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class UserSignUpView(CreateView):
    model = BaseAccount
    form_class = UserSignUpForm
    template_name = 'account/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect('articles:home')

class LogInView(LoginView):
    model = BaseAccount
    form_class = LoginForm
    template_name = 'account/login.html'


class LogOutView(LoginRequiredMixin, LogoutView):
    template_name = 'index.html'