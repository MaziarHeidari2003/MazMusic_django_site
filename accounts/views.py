from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Signup_form, Blog_signup_form
from django.contrib.auth.models import User


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
        return redirect('/')
      
    else:
      messages.add_message(request, messages.ERROR, "Something went wrong,Please try again")
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
    form = Signup_form(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('accounts:login'))
    else:
        for field, errors in form.errors.items():
           messages.add_message(request, messages.ERROR, f"Field {field} has the following errors: {errors}")
           print(f"Field {field} has the following errors: {errors}")
        print('hffgggggggggggggggggggggggggggg')
        
      
  form = Signup_form()
  print('44444444444444444444444444444444444444')
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
  form = Signup_form(request.POST or None, instance=current_user)
  if request.method == 'POST':

    if form.is_valid():
      print('88888888888888888888888888888888888888')
      form.save()
      print('999999999999')
      login(request,current_user)
      print('81111111111111111111118')

      return redirect('/')
    else:
        for field, errors in form.errors.items():
           messages.add_message(request, messages.ERROR, f"Field {field} has the following errors: {errors}")
           return(f"Field {field} has the following errors: {errors}")
        
      
  
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

  return render(request, 'accounts/update_user.html',{
    'form':form
  })


