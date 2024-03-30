from django.shortcuts import render
from accounts.models import Profile
from accounts.forms import Blog_signup_form
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import AbstractUser,User
from blog.forms import Post_form


# Create your views here.
@login_required
def writers_view(request):
    profiles = Profile.objects.all()
    users = User.objects.all()
    logged_user = request.user
    user_pro = False
    if hasattr(logged_user, 'profile'):
      user_pro = True

    profile = Profile.objects.get(user=logged_user)
    if request.method == 'POST':
      form = Blog_signup_form(request.POST,request.FILES,instance=profile)
      if form.is_valid():
        form.save()
        return render(request, 'writers/writer_view.html')

      else:  
        for field, errors in form.errors.items():
          print(f"Field {field} has the following errors: {errors}")
        messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")


    form = Blog_signup_form()
    form.fields['bio'].widget.attrs['class'] = 'single-textarea'
    form.fields['bio'].widget.attrs['placeholder'] = 'a little biography'
    return render(request, 'writers/author-home.html', {
      'profiles':profiles,
      'users':users,
      'form':form,
      'user_pro':user_pro
    }) 
  





def new_post(request):
  if request.method == 'POST':
    form = Post_form(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect('writer _view')
    else:
      for field, errors in form.errors.items():
         print(f"Field {field} has the following errors: {errors}")
         messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")


  try:
    profile = Profile.objects.get(user=request.user)
  except:
     messages.add_message(request, messages.ERROR, "You should be a blog member to have personal page!")
     return redirect ('/')
  
  posts = Post.objects.filter(author=request.user)

  form = Post_form()
  form.fields['title'].widget.attrs['class'] = 'common-input mb-20 form-control'
  form.fields['title'].widget.attrs['placeholder'] = 'Enter the post title'
  form.fields['content'].widget.attrs['class'] = 'common-textarea form-control'
  form.fields['content'].widget.attrs['placeholder'] = 'Enter the content'
  return render(request, 'writers/writer_view.html',{
    'form':form,
    'posts':posts,
    'profile':profile
  })
