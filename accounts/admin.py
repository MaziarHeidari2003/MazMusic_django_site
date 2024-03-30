from django.contrib import admin
from .models import Profile 
# Register your models here.

class Profile_admin(admin.ModelAdmin):

  empty_value_display = 'it is empty'
  list_display = ['user' ]
  list_filter = ['user']




admin.site.register(Profile,Profile_admin)



