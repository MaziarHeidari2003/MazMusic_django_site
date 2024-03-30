from django import forms
from blog.models import Comment,Category,Post


class Comment_form(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content','name','email','post']




class Post_form(forms.ModelForm):

  class Meta:
    model = Post
    fields = ['title','content','author','image','category']



    