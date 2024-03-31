from django.db import models
from blog.models import Category,Post
from django.contrib.auth.models import User


# Create your models here.


class Instructor(models.Model):
  first_name = models.CharField(max_length=200)
  last_name= models.CharField(max_length=200)
  main_instrument = models.ForeignKey(Category, on_delete=models.CASCADE)
  musical_biography = models.TextField()
  image = models.ImageField(default='Bill_Evans')

class Course(models.Model):
  name = models.CharField(max_length=255)
  duration = models.IntegerField()
  content = models.TextField()
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  instructors = models.ManyToManyField(Instructor)
  started_or_not = models.BooleanField(default=False)
  price = models.IntegerField(default=0)
  enrolled_by = models.ManyToManyField(User, blank=True, null=True, related_name='user')




class Performance(models.Model):
  title = models.CharField(max_length=255)
  date = models.DateField()
  place = models.CharField(max_length=255)
  video_file = models.FileField(null=True)
  video_url = models.URLField(blank=True, null=True)
  post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
  instruoctor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

