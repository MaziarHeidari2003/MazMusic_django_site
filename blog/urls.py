from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.blog_view, name='index'),
  path('<int:pid>', views.blog_single, name='single'),
  path('cat/<str:cat_name>', views.blog_view, name='category'),
  path('search',views.blog_search, name='search'),
  path('author/<str:author_name>',views.blog_view, name='author')


  
]