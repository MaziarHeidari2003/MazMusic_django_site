from .models import User_message
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm



class User_message_form(ModelForm):
  class Meta:
    model=User_message
    fields= ['message','user_name','email','subject']