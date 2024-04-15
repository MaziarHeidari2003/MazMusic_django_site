from django.shortcuts import render,redirect
from .models import Course,Instructor,User_message
from .forms import User_message_form
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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
      """
      send_mail(
                subject=request.POST.get('subject'),
                message=request.POST.get('message'),
                from_email=request.POST.get('email'),
                recipient_list=['maziarheidari1124@gmail.com'],
                fail_silently=False
           )
           """
      my_subject = 'Email from maz_music'
      my_receptient = form.cleaned_data['email']
      html_message = render_to_string('website/email.html')
      plain_message = strip_tags(html_message)

      message = EmailMultiAlternatives(
        subject= my_subject,
        body=plain_message,
        from_email=request.POST.get('email'),
        to=[my_receptient],

      )

      message.attach_alternative(html_message,'text/html')
      message.send()

      messages.add_message(request, messages.SUCCESS, "Thanks for your message, we'll respond shortly ")
      return HttpResponseRedirect(reverse('website:contact'))
    else:
      messages.add_message(request, messages.WARNING, "Sorry, Something went wrong, please try again")
      return HttpResponseRedirect(reverse('website:contact'))

  form=User_message_form()
  return render(request, 'website/contact.html', {
    'form':form
  })