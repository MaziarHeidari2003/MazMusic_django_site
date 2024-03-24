from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages


# Create your views here.


def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      messages.add_message(request, messages.ERROR, "Something went wrong,Please try again")
  return render(request, 'accounts/login.html')



def signup_view(request):
  return render(request, 'accounts/signup.html')