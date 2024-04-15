from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Signup_form, Blog_signup_form,Update_user_form,Change_password_form
from django.contrib.auth.models import User
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request,user)
        if 'next' in request.POST:
          print(request.POST.get('next'))
          return redirect(request.POST.get('next'))
       
        return redirect('/')
      
    else:
        for error in list(form.errors.values()):
          messages.error(request,error)    
  form = AuthenticationForm()    
  form.fields['password'].widget.attrs['class'] = 'input100'
  form.fields['username'].widget.attrs['class'] = 'input100'
  form.fields['username'].widget.attrs['placeholder'] = 'Username'
  form.fields['password'].widget.attrs['placeholder'] = 'Password'
  form.fields['username'].widget.attrs['background-color'] = 'white'
  form.fields['password'].widget.attrs['background-color'] = 'white'

  return render(request, 'accounts/login.html', {
    'form':form
  })


@login_required
def logout_view(request):
  logout(request)
  return redirect('/')



def signup_view(request):
  if request.method == 'POST':
    if request.method == 'POST':
      form = Signup_form(request.POST)
      if form.is_valid():
        form.save()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password1')
        user = authenticate(request, username=username, password=password)
        login(request,user)
        my_subject = 'Email from maz_music'
        my_receptient = form.cleaned_data['email']
        mail_user = User.objects.get(email=my_receptient)
        welcome_message = 'Welcome to maz_music Dear '+ str(user.first_name.capitalize())+'!' 


        html_message = render_to_string('website/email.html',{
          'welcome_message':welcome_message
        })
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
          subject= my_subject,
          body=plain_message,
          from_email=request.POST.get('email'),
          to=[my_receptient],

        )

        message.attach_alternative(html_message,'text/html')
        message.send()
        return redirect('/')
      else:
            for error in list(form.errors.values()):
                messages.error(request,error)    
          
      
  form = Signup_form()
  """
    form.fields['image'].widget.attrs['class'] = 'btn'
  form.fields['email'].widget.attrs['class'] = 'input100'
  form.fields['email'].widget.attrs['placeholder'] = 'checkcorea@gmail.com'
  form.fields['first_name'].widget.attrs['class'] = 'input100'
  form.fields['last_name'].widget.attrs['class'] = 'input100'
  """
  form.fields['password1'].widget.attrs['class'] = 'input100'
  form.fields['password2'].widget.attrs['class'] = 'input100'
  form.fields['username'].widget.attrs['class'] = 'input100'
  form.fields['username'].widget.attrs['placeholder'] = 'ChickCorea1941'
  form.fields['password1'].widget.attrs['placeholder'] = '********'
  form.fields['password2'].widget.attrs['placeholder'] = '********'
  form.fields['email'].widget.attrs['class'] = 'input100'
  form.fields['email'].widget.attrs['placeholder'] = 'checkcorea@gmail.com'
  form.fields['first_name'].widget.attrs['class'] = 'input100'
  form.fields['last_name'].widget.attrs['class'] = 'input100'
  return render(request, 'accounts/signup.html',{
    'form':form
  })



@login_required
def update_profile(request):
  current_user = User.objects.get(id=request.user.id)
  form = Update_user_form(request.POST or None, instance=current_user)
  if request.method == 'POST':

    if form.is_valid():
      form.save()
      login(request,current_user)

      return redirect('/')
    else:
        for field, errors in form.errors.items():
           messages.add_message(request, messages.ERROR, f"Field {field} has the following errors: {errors}")
           print(f"Field {field} has the following errors: {errors}")
        
  form.fields['username'].widget.attrs['class'] = 'input100'
  form.fields['username'].widget.attrs['placeholder'] = 'ChickCorea1941'
  form.fields['email'].widget.attrs['class'] = 'input100'
  form.fields['email'].widget.attrs['placeholder'] = 'checkcorea@gmail.com'
  form.fields['first_name'].widget.attrs['class'] = 'input100'
  form.fields['last_name'].widget.attrs['class'] = 'input100'

  return render(request, 'accounts/update_user.html',{
    'form':form
  })


@login_required
def update_password(request):
  current_user = request.user
  if request.method == 'POST':
    form = Change_password_form(current_user,request.POST)

    if form.is_valid():
      form.save()
      messages.success(request,'Your Password Has Been Updated')
      login(request,current_user)
      return redirect('/')
      
    # something nice to handle the else part with exact messages
    else:
      for error in list(form.errors.values()):
        messages.error(request,error)    
      return HttpResponseRedirect(reverse('accounts:update_password'))  
  form = Change_password_form(current_user)
  form.fields['new_password1'].widget.attrs['class'] = 'input100'
  form.fields['new_password2'].widget.attrs['class'] = 'input100'
  form.fields['new_password1'].widget.attrs['placeholder'] = 'Enter new password'
  form.fields['new_password2'].widget.attrs['placeholder'] = 'Enter again'

  return render (request, 'accounts/update_password.html', {
    'form':form
  })

