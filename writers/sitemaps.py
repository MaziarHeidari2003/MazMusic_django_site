from django.contrib.sitemaps import Sitemap
from accounts.models import Profile
from django.urls import reverse

class WritersSitemap(Sitemap):
  changefreq = 'daily'
  priority = 0.5


  def items(self):
    return Profile.objects.all()
  
  def lastmod(self,obj):
    return obj.user.last_login
  
  def location(self,item):
        return reverse('writers:writer_view')