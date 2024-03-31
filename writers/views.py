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
        return redirect(request.path)

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
  




@login_required
def new_post(request):
  profile = Profile.objects.get(user=request.user)
  posts = Post.objects.filter(author=request.user)
  if request.method == 'POST':
    if request.POST.get('form_type') == 'its_post':
      print(request.POST)
      form = Post_form(request.POST,request.FILES)
      if form.is_valid():
        form.save()
        return redirect('/')
      else:
        for field, errors in form.errors.items():
          print(f"Field {field} has the following errors: {errors}")
          messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")

    elif request.POST.get('form_type') == 'its_bio':
        
        form = Blog_signup_form(request.POST or None,request.FILES or None,instance=profile)
        if form.is_valid():
          form.save()
          return redirect(request.path)

        else:  
          for field, errors in form.errors.items():
            print(f"Field {field} has the following errors: {errors}")
          messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")



  profile = Profile.objects.get(user=request.user)
  posts = Post.objects.filter(author=request.user)
  form = Post_form()
  form.fields['title'].widget.attrs['class'] = 'common-input mb-20 form-control'
  form.fields['title'].widget.attrs['placeholder'] = 'Enter the post title'
  form.fields['content'].widget.attrs['class'] = 'common-textarea form-control'
  form.fields['content'].widget.attrs['placeholder'] = 'Enter the content'
  form.fields['category'].widget.attrs['class'] = 'form-group'




  bform = Blog_signup_form()
  bform.fields['bio'].widget.attrs['class'] = 'single-textarea'
  bform.fields['bio'].widget.attrs['placeholder'] = 'a little biography'




  return render(request, 'writers/writer_view.html',{
    'form':form,
    'posts':posts,
    'profile':profile,
    'bform':bform
  })











