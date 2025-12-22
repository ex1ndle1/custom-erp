from django.contrib import admin
from django.urls import path, include
from .views import register, activate, oauth_register

app_name = 'user'

urlpatterns = [
      path('accounts/', include('allauth.urls')),
  path('register/' , register , name='register'),
  path('activate/<uidb64>/<token>/', activate ,name='activate'),
  path('oauth_register/' , oauth_register , name='oauth_register'),

]