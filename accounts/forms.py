from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class Signup_form(UserCreationForm):
  """
  email = forms.EmailField()
  last_name= forms.CharField(max_length=120)
  image= forms.ImageField()

  """
  first_name = forms.CharField(max_length=120)
  last_name = forms.CharField(max_length=120)
  email= forms.EmailField()



  class Meta:
    model = User
    fields = ['username','password1','password2','first_name','last_name','email']	