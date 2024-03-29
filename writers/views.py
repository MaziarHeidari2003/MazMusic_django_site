from django.shortcuts import render
from accounts.models import Profile
from accounts.forms import Blog_signup_form
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post


# Create your views here.


def writers_view(request):
  profiles = Profile.objects.all()
  logged_user = request.user
  user_pro = False
  if hasattr(logged_user, 'profile'):
    user_pro = True
  if request.method == 'POST':
    form = Blog_signup_form(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return render(request, 'writers/post-creation.html')

    else:  
      for field, errors in form.errors.items():
        print(f"Field {field} has the following errors: {errors}")
      messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")


  form = Blog_signup_form()
  form.fields['first_name'].widget.attrs['class'] = 'single-input'
  form.fields['first_name'].widget.attrs['placeholder'] ='First Name'
  form.fields['first_name'].widget.attrs['onfocus'] ="this.placeholder = ''"
  form.fields['first_name'].widget.attrs['onblur'] ="this.placeholder = 'First Name'" 
  form.fields['bio'].widget.attrs['class'] = 'single-textarea'
  form.fields['bio'].widget.attrs['placeholder'] = 'a little biography'
  form.fields['last_name'].widget.attrs['class'] = 'single-input'
  form.fields['last_name'].widget.attrs['placeholder'] ='Last Name'


  return render(request, 'writers/author-home.html', {
    'profiles':profiles,
    'form':form,
    'user_pro':user_pro
  })    



def writer_posts_view(request):
  try:
    profile = Profile.objects.get(user=request.user)
  except:
     messages.add_message(request, messages.ERROR, "You should be a blog member to have personal page!")
     return redirect ('/')
  
  posts = Post.objects.filter(author=request.user)
  return render (request, 'writers/writer_view.html',{
    'posts':posts,
    'profile':profile
  })



