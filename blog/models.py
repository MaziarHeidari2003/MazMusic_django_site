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

  def __str__(self):
    return self.name


class Musician(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  birth_date = models.DateField()
  death_date = models.DateField(null=True, blank=True)
  legend = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  





class Post(models.Model):
  title = models.CharField(max_length=255)
  musician = models.ForeignKey(Musician, models.CASCADE)
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
    musician = models.ForeignKey(Musician, models.CASCADE)
    audio_file = models.FileField(default='D:/Programming/Start_Web_Programming_CS50/maz_music/media/Lilac.mp3')
    audio_url = models.URLField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
      return self.title




class Performance(models.Model):
  date = models.DateField()
  place = models.CharField(max_length=255)
  performer = models.ForeignKey(Musician, models.CASCADE)
  track = models.ForeignKey(Track, models.CASCADE)
  video_file = models.FileField(null=True)
  video_url = models.URLField(blank=True, null=True)
  post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f'{self.track} played by {self.performer}'



class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
  # comment_author = models.ForeignKey(ArticleForm, on_delete=models.CASCADE, related_name='comments')
 #  commenter_name = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=255)
   email = models.EmailField()
   content = models.TextField()
   created_date = models.DateTimeField(auto_now_add=True)
   approved = models.BooleanField(default=False)


   def __str__(self):
       return "'{}' commented by '{}'".format(self.content, self.name)

   class Meta:
       ordering = ['-created_date']



class Reply_comment(models.Model):
   reply_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
   replier_name = models.ForeignKey(User, on_delete=models.CASCADE)
   reply_content = models.TextField()
   replied_date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return "'{}' replied with '{}' to '{}'".format(self.replier_name,self.reply_content, self.reply_comment)

