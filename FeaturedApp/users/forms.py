from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta: #This class specifies how we want our fields to be shown It keeps configurations in one place   and within the same class
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 