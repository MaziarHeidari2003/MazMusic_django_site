from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        if self.profile_picture:
            # Use the user's username as part of the image file path
            # You can customize the file path as per your requirements
            self.profile_picture.storage.delete(self.profile_picture.name)
            self.profile_picture.storage.save(self.user.username + '.jpg', self.profile_picture)

        super(Profile, self).save(*args, **kwargs)



"""




class Category(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(default='Chick_Corea.jpg')

  def __str__(self):
    return self.name






class Post(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField()
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  counted_views = models.IntegerField(default=1)
  category = models.ManyToManyField(Category)
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  approved = models.BooleanField(default=False)
  likes = models.ManyToManyField(User, related_name='blog_post')

  def total_likes(self):
     return self.likes.count()


  class Meta:
     ordering = ['published_date']

  def __str__(self):
    return self.title
  

class Track(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    audio_file = models.FileField(default='D:/Programming/Start_Web_Programming_CS50/maz_music/media/Lilac.mp3')
    audio_url = models.URLField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
      return self.title








