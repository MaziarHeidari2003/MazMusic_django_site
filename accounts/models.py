from django.contrib.auth.models import AbstractUser,User
from django.db import models

# Create your models here.



    # Your model fields...


class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
  image = models.ImageField(default='default_profile.png',blank=True, null=True)
  bio = models.TextField(default='No Bio yet...', blank=True)








 
"""





class CustomUser(User):
    
    
 
    def get_profile_info(self):
        profile = Profile.objects.filter(user=self).first()

        if profile:
            # Access any profile fields here
            return {
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'bio': profile.bio,  
                'image':profile.image
              }
        else:
            # Return basic user info if no profile exists
          return {
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
            }
"""