from django import template
from blog.models import Post,Category,Comment
from django.db.models import Count



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