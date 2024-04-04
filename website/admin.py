from django.contrib import admin
from .models import Instructor, Course,Performance,User_message
# Register your models here.

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Performance)
admin.site.register(User_message)