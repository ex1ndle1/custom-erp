from django.contrib import admin
from django.urls import path, include
from .views import index,CorsesViewPage,DetailViewPage


app_name = 'erp'

urlpatterns = [
 path('home/', index , name='home'),
 path('courses/',CorsesViewPage.as_view(), name='courses'),
 path('detail/<int:course_id>', DetailViewPage.as_view(), name='detail'),

]
