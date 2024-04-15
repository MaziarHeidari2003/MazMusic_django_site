from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Track,Category
from comment.models import Comment, Reply
from accounts.models import Profile
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from comment.forms import Comment_form,Reply_form
from django.contrib.auth.decorators import login_required


# Create your views here.

def like_view(request, pid):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))
  liked = False
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)
    liked=False
  else:    
    post.likes.add(request.user)
    liked=True
  return HttpResponseRedirect(reverse('blog:single', args=[str(pid)]))




def comment_delete_view(request, pk):
        comment = get_object_or_404(Comment, id=pk, commenter=request.user)
        post_id = comment.post.id 
        comment.delete()  # Delete the comment from the database
        return HttpResponseRedirect(reverse('blog:single', args=(post_id,)))




def blog_view(request, **kwargs):
  posts = Post.objects.all()
  categories = Category.objects.all()

  if kwargs.get('cat_name') != None:
    posts = posts.filter(category__name=kwargs['cat_name'])
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

  if kwargs.get('author_name') != None: 
    posts = posts.filter(author__username=kwargs['author_name'])
    profile = Profile.objects.get(user__username=kwargs['author_name'])
    posts = Paginator(posts,3)
    try:
      page_number = request.GET.get('page')
      posts = posts.get_page(page_number)
    except PageNotAnInteger:
      posts = posts.get_page(1)
    except EmptyPage:
      posts = posts.get_page(1)  

    return render(request, 'blog/blog-author.html',{
      'posts':posts,
      'categories':categories,
      'profile':profile
    })
  posts = Paginator(posts,5)
  try:
      page_number = request.GET.get('page')
      posts = posts.get_page(page_number)
  except PageNotAnInteger:
      posts = posts.get_page(1)
  except EmptyPage:
      posts = posts.get_page(1)  

  return render(request, 'blog/blog-home.html',{
      'posts':posts,
      'categories':categories,
    })





def blog_single(request,pid):
  post = Post.objects.get(pk=pid)
  current_user = request.user
  comments = Comment.objects.filter(post=post).order_by('-date')
  comments_count = comments.count()
  replies_count = Reply.objects.filter(parent_comment__post=post).count()
  total_comments = replies_count+comments_count
  if request.method == 'POST':
    if request.POST.get('form_type') == 'its_comment':

      form = Comment_form(request.POST, request.FILES)
      if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.commenter = current_user
        comment.save()
        return HttpResponseRedirect(reverse('blog:single',args=(post.id,)))
      else:
        for errors,feild in form.errors.items():
          print(f'{errors} in {feild}')

  form = Comment_form()
  form.fields['content'].widget.attrs['class'] = 'form-control mb-10'
  form.fields['content'].widget.attrs['rows'] = '5'
  rform = Reply_form()
  rform.fields['content'].widget.attrs['class'] = 'form-control mb-10'
  rform.fields['content'].widget.attrs['style'] = 'height:25px;'

  rform.fields['content'].widget.attrs['rows'] = '5'
  rform.fields['content'].widget.attrs['width'] = '100%'

  categories = Category.objects.all()
  profile = Profile.objects.get(user=post.author)
  tracks = Track.objects.filter(post=post.id)

  liked = False
  if post.likes.filter(id=request.user.id).exists():
    liked=True


  return render(request, 'blog/blog-single.html', {
    'form':form,
    'rform':rform,
    'comments':comments,
      'post':post,
      'tracks':tracks,
      'categories':categories,
      'liked':liked,
      'profile':profile,
      'request':request,
      'total_comments':total_comments
    })


@login_required
def reply_comment(request,pk):
  comment = get_object_or_404(Comment,id=pk)
  post =  comment.post.id

  if request.method == 'POST':
    if request.POST.get('form_type') == 'its_reply':
      print(request.POST.get('form_type'))

      form = Reply_form(request.POST,request.FILES)
      print(request.POST.get('form_type'))

      if form.is_valid():
        reply = form.save(commit=False)
        reply.replier = request.user
        reply.parent_comment=comment
        reply.save()
      else:
        for field, errors in form.errors.items():
          print(f"Field {field} has the following errors: {errors}")

      return HttpResponseRedirect(reverse('blog:single',args=(post,)))
  return HttpResponseRedirect(reverse('blog:single',args=(post,)))



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


