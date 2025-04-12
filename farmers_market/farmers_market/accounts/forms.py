from django import forms
from django.contrib.auth.forms import UserCreationForm
from .model import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'location', 'password1', 'password2']
