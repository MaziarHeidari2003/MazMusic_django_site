from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Signup_form


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

  
  if request.method == 'GET':    
    form = Signup_form()
    print('44444444444444444444444444444444444444')
    form.fields['email'].widget.attrs['class'] = 'input100'
    form.fields['email'].widget.attrs['placeholder'] = 'checkcorea@gmail.com'
    form.fields['first_name'].widget.attrs['class'] = 'input100'
    form.fields['last_name'].widget.attrs['class'] = 'input100'
    form.fields['image'].widget.attrs['class'] = 'btn'
    form.fields['password1'].widget.attrs['class'] = 'input100'
    form.fields['password2'].widget.attrs['class'] = 'input100'
    form.fields['username'].widget.attrs['class'] = 'input100'
    form.fields['username'].widget.attrs['placeholder'] = 'ChickCorea1941'
    form.fields['password1'].widget.attrs['placeholder'] = '********'
    form.fields['password2'].widget.attrs['placeholder'] = '********'



  if request.method == 'POST':
    form = Signup_form(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('accounts:login'))
    else:
       print('hffgggggggggggggggggggggggggggg')
       messages.add_message(request, messages.ERROR, "Something went wrong, please try again!")


  return render(request, 'accounts/signup.html',{
    'form':form
  })