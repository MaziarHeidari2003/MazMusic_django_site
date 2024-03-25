from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Signup_form(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length=120)
  last_name= forms.CharField(max_length=120)
  image= forms.ImageField()

  class Meta:
    model = User
    fields = ['username','first_name','last_name','email','password1','password2','image']	