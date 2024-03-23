from django import forms
from blog.models import Comment


class Comment_form(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content','name','email','post']