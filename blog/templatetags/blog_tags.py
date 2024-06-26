from django import template
from blog.models import Post,Category
from accounts.models import Profile
from django.db.models import Count
import random
from urllib.parse import unquote
from comment.models import Comment,Reply



register = template.Library()




@register.simple_tag
def get_current_url(request):
    return unquote(request.build_absolute_uri())

@register.inclusion_tag('blog/post-categories.html')
def post_categories():
  category_counts = Category.objects.annotate(
  post_count=Count('post'))
  cat_dict = {}
  for category in category_counts:
    category_name = category.name
    post_count = category.post_count
    cat_dict[category_name] = post_count

  return {
    'categories':cat_dict
  }



@register.inclusion_tag('blog/popular.html')
def popular_posts():
  posts = Post.objects.filter(approved=True).order_by('-counted_views')[:4]
  return {
    'posts':posts
  }



@register.simple_tag(name='comments_count')
def func(pid):
    post = Post.objects.get(id=pid)
    comments = Comment.objects.filter(post=post)
    comments_count = comments.count()
    replies_count = Reply.objects.filter(parent_comment__post=post).count()
    total_comments = replies_count+comments_count
    return total_comments




@register.inclusion_tag('website/latest_posts.html')
def latest_posts():
  posts = Post.objects.filter(approved=True)[:5]
  return {
    'posts':posts
  }


@register.inclusion_tag('blog/writer.html')
def writer_page(pid):
  profile = Profile.objects.filter(user=pid)
  posts = Post.objects.filter(author=pid)
  return {
    'posts':posts,
    'profile':profile
  }


@register.inclusion_tag('blog/random_categories.html')
def top_categories():
     categories = list(Category.objects.all())
     random.shuffle(categories)

     random_categories = categories[:3]
     return {
      'random_categories':random_categories
    }


    #it is for making the first letter of the names of the users capitalize

@register.filter()
def upfirstletter(value):
    first = value[0] if len(value) > 0 else ''
    remaining = value[1:] if len(value) > 1 else ''
    return first.upper() + remaining


#to remove some info wich is behind the iage button 

@register.filter
def remove_clear_text(value):
    return '' if value == 'Clear' else value






