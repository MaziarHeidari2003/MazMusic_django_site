from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError


class Signup_form(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password1 = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm password', max_length=100, widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise ValidationError('Passwords do not match.')

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Your email validation logic here, e.g., checking if email is already taken
        
        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email address is already in use.')

        # Check if the email follows the correct format
      
        return email


class Blog_signup_form(ModelForm):
  class Meta:
    model = Profile
    fields = ['bio','image','user']
