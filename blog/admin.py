from django.contrib import admin
from .models import Category,Post,Track

# Register your models here.



class Post_admin(admin.ModelAdmin):
  date_hierarchy = 'published_date'
  empty_value_display = 'it is empty'
  list_display = ['title', 'author', 'counted_views', 'approved', ]
  list_filter = ['approved', 'author']
  


admin.site.register(Category)
admin.site.register(Post, Post_admin)
admin.site.register(Track)


