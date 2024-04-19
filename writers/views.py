from django.shortcuts import render
from accounts.models import Profile
from accounts.forms import Blog_signup_form
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post,Category
from django.contrib.auth.models import AbstractUser,User
from blog.forms import Post_form
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
def writers_view(request):
    profiles = Profile.objects.all()
    users = User.objects.all()
    logged_user = request.user
    user_pro = False
    if hasattr(logged_user, 'profile'):
      user_pro = True
    try:
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

      users = Paginator(users,6)
      try:
        page_number=request.GET.get('page')
        users = users.get_page(page_number)
      except PageNotAnInteger:
        users=users.get_page(1)
      except EmptyPage:
        users = users.get_page(1)    
      return render(request, 'writers/author-home.html', {
      'users':users,
      'form':form,
      'user_pro':user_pro
    }) 
  
    except:
         return render(request, 'writers/author-home.html', {
      'profiles':profiles,
      'users':users,
      'user_pro':user_pro
       }) 



@login_required
def new_post(request):
  profile = Profile.objects.get(user=request.user)
  posts = Post.objects.filter(author=request.user)
  profile = Profile.objects.get(user=request.user)
  posts = Post.objects.filter(author=request.user)
  form = Post_form()
  form.fields['title'].widget.attrs['class'] = 'common-input mb-20 form-control'
  form.fields['title'].widget.attrs['placeholder'] = 'Enter the post title'
  form.fields['content'].widget.attrs['class'] = 'common-textarea form-control'
  form.fields['content'].widget.attrs['placeholder'] = 'Enter the content'
  form.fields['category'].widget.attrs['class'] = 'form-group'

  bform = Blog_signup_form(request.POST or None,request.FILES or None,instance=profile)
  bform.fields['bio'].widget.attrs['class'] = 'common-textarea form-control'
  bform.fields['bio'].widget.attrs['placeholder'] = 'a little biography'
  bform.fields['bio'].widget.attrs['onfocus'] = "this.placeholder = ''"
  bform.fields['bio'].widget.attrs['onblur'] =  "this.placeholder = 'Enter Bio'"
  bform.fields['bio'].widget.attrs['style'] =  "width: 260px; height: 160px;"



  if request.method == 'POST':
    if request.POST.get('form_type') == 'its_post':
      print(request.POST)
      form = Post_form(request.POST,request.FILES)
      if form.is_valid():
        form.save()
        
        return render(request, 'writers/writer_view.html',{
          'form':form,
          'posts':posts,
          'profile':profile,
          'bform':bform,
        })


      else:
        for field, errors in form.errors.items():
          print(f"Field {field} has the following errors: {errors}")
          messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")



  return render(request, 'writers/writer_view.html',{
    'form':form,
    'posts':posts,
    'profile':profile,
    'bform':bform,
  })







def the_bio_form(request):
    profile = Profile.objects.get(user=request.user.id)

    if request.method == 'POST':
      print('bitch')
      if request.POST.get('form_type') == 'its_bio':
          form = Blog_signup_form(request.POST or None,request.FILES or None,instance=profile)
          if form.is_valid():  
            form.save()
            return HttpResponseRedirect(reverse('writers:writer_view'))

          else:  
            for field, errors in form.errors.items():
              print(f"Field {field} has the following errors: {errors}")
            messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")



