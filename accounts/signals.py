from django.dispatch import receiver
from django.db.models.signals import (
  post_save,
)
from django.contrib.auth.models import AbstractUser,User
from .models import Profile
from django.db.models.signals import pre_save




@receiver(post_save, sender=User)
def update_user_profile(sender,instance,created, **kwargs):
  if created:
    Profile.objects.create(
      user=instance
    )




