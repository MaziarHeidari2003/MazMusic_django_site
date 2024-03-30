from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.forms import ModelForm

class Signup_form(UserCreationForm):
  """
  email = forms.EmailField()
  last_name= forms.CharField(max_length=120)
  image= forms.ImageField()

  """
  
  email= forms.EmailField()



  class Meta:
    model = User
    fields = ['username','password1','password2','email','first_name', 'last_name']	



class Blog_signup_form(ModelForm):
  class Meta:
    model = Profile
    fields = ['bio','image','user']
