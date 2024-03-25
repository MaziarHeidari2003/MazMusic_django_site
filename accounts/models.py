from django.contrib.auth.models import AbstractUser,User
from django.db import models

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
  image = models.ImageField(blank=True, null=True)