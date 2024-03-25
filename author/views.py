from django.shortcuts import render

# Create your views here.

def writers(request):
  return render(request, 'authors/author-home.html')