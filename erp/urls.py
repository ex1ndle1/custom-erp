from django.contrib import admin
from django.urls import path, include
from .views import index,CorsesViewPage,DetailViewPage, SubjectViewPage


app_name = 'erp'

urlpatterns = [
 path('home/', index , name='home'),
 path('courses/',CorsesViewPage.as_view(), name='courses'),
 path('detail/<int:course_id>', DetailViewPage.as_view(), name='detail'),
 path('subject/<int:subject_id>',SubjectViewPage.as_view(), name='subject' )

]
