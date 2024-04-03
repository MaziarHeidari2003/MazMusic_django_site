from django.shortcuts import render
from .models import Course,Instructor

# Create your views here.


def index_view(request):
  courses = Course.objects.all()
  return render(request, 'website/index.html', {
    'courses':courses
  })

def about_view(request):
  return render(request, 'website/about.html')

def contact_view(request):
  return render(request, 'website/contact.html')