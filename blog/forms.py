from django import forms
from blog.models import Comment,Category


class Comment_form(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content','name','email','post']




class Post_form(forms.ModelForm):
  author= forms.CharField(max_length=255)
  title = forms.CharField(max_length=255)
  image = forms.ImageField()
  content = forms.CharField(widget=forms.Textarea())
  category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))


    