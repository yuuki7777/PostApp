from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BaseAccount

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = BaseAccount
        fields = ['username','email','password1','password2']

        def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
                return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = BaseAccount
        fields = ['username', 'password']