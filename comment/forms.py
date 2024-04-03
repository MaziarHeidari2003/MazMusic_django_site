from django import forms
from .models import Comment,Reply


class Comment_form(forms.ModelForm):
  content = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'enter comment'}), required=True)

  class Meta:
    model = Comment
    fields = ['content']


class Reply_form(forms.ModelForm):
  class Meta:
    model = Reply
    fields =['content']
    widgets = {
      'content': forms.TextInput(attrs={'placeholder':'Add reply ...'})
    }