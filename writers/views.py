from django.shortcuts import render
from accounts.models import Profile

# Create your views here.


def writers_view(request):
  profiles = Profile.objects.all()

  return render(request, 'writers/author-home.html', {
    'profiles':profiles
  })    


