from django.urls import path, include
from . import views

app_name = 'author'

urlpatterns = [
  path('writers', views.writers, name='writers'),
  
  
  
]