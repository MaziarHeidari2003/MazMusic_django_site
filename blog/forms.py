from django import forms
from blog.models import Category,Post




class Post_form(forms.ModelForm):

  class Meta:
    model = Post
    fields = ['title','content','author','image','category']



    