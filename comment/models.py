from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
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