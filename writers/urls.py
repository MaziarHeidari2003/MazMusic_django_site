from django.urls import path, include
from . import views

app_name = 'writers'

urlpatterns = [
  path('', views.writers_view, name='index'),
  path('post_creation', views.writers_view, name='membership'),
  path('writer_view',views.new_post, name='writer_view')

 

  
]