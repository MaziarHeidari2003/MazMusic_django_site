from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.shortcuts import get_object_or_404,redirect
# Create your models here.

class Comment(models.Model):
  commenter = models.ForeignKey(User,on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    try:
      return f'{self.commenter.username} : {self.content[:40]}'
    except:
      return f'no author : {self.content[:30]}'
    
  
class Reply(models.Model):
  replier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies')
  
  parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
  content = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    try:
      return f'{self.replier.username} : {self.content[:40]}'
    except:
      return f'no author : {self.content[:40]}'  

  class Meta:
    ordering = ['date']