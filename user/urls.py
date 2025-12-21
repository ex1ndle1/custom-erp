from django.contrib import admin
from django.urls import path, include
from .views import register, activate

app_name = 'user'

urlpatterns = [
  path('register/' , register , name='register'),
  path('activate/<uidb64>/<token>/', activate ,name='activate'),
]