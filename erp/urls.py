from django.contrib import admin
from django.urls import path, include
from .views import index


app_name = 'erp'

urlpatterns = [
 path('home/', index , name='home')

]
