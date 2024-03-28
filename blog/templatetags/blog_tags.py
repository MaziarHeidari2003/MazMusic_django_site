from django import template
from blog.models import Post,Category,Comment
from accounts.models import Profile
from django.db.models import Count
import random



register = template.Library()


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
  post = Post.objects.get(pk=pid)
  return Comment.objects.filter(post=post.id, approved=True).count()





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
    cat_num = Category.objects.count()
    x = random.sample(range(1, cat_num), 3)
    categories = Category.objects.filter(id__in=x)
    return {
      'random_categories':categories
    }


    

