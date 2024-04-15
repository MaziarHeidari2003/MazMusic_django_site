from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
  path('login', views.login_view, name='login'),
  path('signup', views.signup_view, name='signup'),
  path('logout', views.logout_view, name='logout'),
  path('update_user',views.update_profile, name='update_profile'),
  path('update_password',views.update_password, name='update_password')

  
]