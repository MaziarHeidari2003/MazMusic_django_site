from django.shortcuts import render,redirect
from .models import Course,Instructor,User_message
from .forms import User_message_form
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index_view(request):
  courses = Course.objects.all()
  return render(request, 'website/index.html', {
    'courses':courses
  })



def single_course(request,cid):
  course = Course.objects.get(id=cid)
  return render(request, 'website/single-course.html',{
    'course':course
  })





def about_view(request):
  return render(request, 'website/about.html')



def contact_view(request):
  if request.method == 'POST':
    form = User_message_form(request.POST, request.FILES)
    if form.is_valid():
      form.save()
     
      send_mail(
                request.POST.get('user_name'),
                request.POST.get('message'),
                request.POST.get('email'),
                ['maziarheidari1124@gmail.com']
           )
      messages.add_message(request, messages.ERROR, f" ")
      return HttpResponseRedirect(reverse('website:contact'))
    else:
      for field, errors in form.errors.items():
          messages.add_message(request, messages.ERROR, f"Field {field} has the following errors: {errors}")
          print(f"Field {field} has the following errors: {errors}")
  form=User_message_form()
  return render(request, 'website/contact.html', {
    'form':form
  })