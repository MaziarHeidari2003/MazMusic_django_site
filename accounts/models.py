from django.contrib.auth.models import AbstractUser,User
from django.db import models

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
  image = models.ImageField(default='default_profile',blank=True, null=True)
  bio = models.TextField(null=True, blank=True)
  first_name = models.CharField(max_length=120,default='someone')
  last_name = models.CharField(max_length=120,default='someone')


  def __str__(self):
    return f'{self.first_name} {self.last_name}'