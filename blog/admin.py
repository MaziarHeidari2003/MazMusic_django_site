from django.contrib import admin
from .models import Category,Post,Track, Performance,Comment 

# Register your models here.



class Post_admin(admin.ModelAdmin):
  date_hierarchy = 'published_date'
  empty_value_display = 'it is empty'
  list_display = ['title', 'author', 'counted_views', 'approved', ]
  list_filter = ['approved', 'author']
  

class Comment_admin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  empty_value_display = 'it is empty'
  list_display = ['name', 'approved','created_date' ]
  list_filter = ['approved', 'post']


admin.site.register(Category)
admin.site.register(Performance)
admin.site.register(Post, Post_admin)
admin.site.register(Comment,Comment_admin)
admin.site.register(Track)


