from django.shortcuts import render
from .models import Post,Track,Category,Musician,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.forms import Comment_form


# Create your views here.


def blog_view(request, **kwargs):
  posts = Post.objects.all()
  categories = Category.objects.all()
  musician = Musician.objects.all()

  if kwargs.get('cat_name') != None:
    posts = posts.filter(category__name=kwargs['cat_name'])

  if kwargs.get('author_name') != None:
    posts = posts.filter(author__username=kwargs['author_name'])

  posts = Paginator(posts,3)
  try:
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
  except PageNotAnInteger:
     posts = posts.get_page(1)
  except EmptyPage:
     posts = posts.get_page(1)  



  return render(request, 'blog/blog-home.html',{
    'posts':posts,
    'categories':categories
  })



def blog_single(request,pid):

  if request.method == 'POST':
    form = Comment_form(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, "Your comment added succesfully")

    else:
       messages.add_message(request, messages.ERROR, "Something went wrong with ypur comment!")


  categories = Category.objects.all()
  post = Post.objects.get(pk=pid)
  tracks = Track.objects.filter(post=post.id)
  form = Comment_form()
  comments = Comment.objects.filter(post=post.id, approved=True)
  return render(request, 'blog/blog-single.html', {
      'post':post,
      'tracks':tracks,
      'categories':categories,
      'comments':comments,
      'form':form
    })



def blog_search(request):
    posts = Post.objects.all()
    if request.method == 'GET':
      if s := request.GET.get('s'):
        if posts := posts.filter(content__contains=s):
          messages.add_message(request, messages.SUCCESS, "Search results, all for you!")
          return render(request, 'blog/blog-home.html', {
          'posts':posts,
          })

        else:
            messages.add_message(request, messages.WARNING, "Sorry,no results were found")
            posts = Post.objects.all()
            return render(request, 'blog/blog-home.html', {
          'posts':posts,

          })


