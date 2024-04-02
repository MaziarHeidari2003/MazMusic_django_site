from django import forms
from .models import Comment


class Comment_form(forms.ModelForm):
  content = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'enter comment'}), required=True)

  class Meta:
    model = Comment
    fields = ['content']