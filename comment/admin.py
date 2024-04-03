from django.contrib import admin
from .models import Comment,Reply

# Register your models here.

admin.site.register(Comment)
admin.site.register(Reply)