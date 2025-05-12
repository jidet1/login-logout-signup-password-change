from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Create your models here.
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=63)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
