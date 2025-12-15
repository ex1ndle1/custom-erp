from django.shortcuts import render
from .models import Course
# Create your views here.
from django.views.generic import DetailView,ListView
from .models import Course



def index(request):
    course = Course.objects.all()
    return render(request , 'erp/index.html', {'courses':course})


class DetailViewPage(DetailView):
    model = Course
    template_name = 'erp/detail.html'
    context_object_name = 'course'
    pk_url_kwarg = 'course_id'
   



class CorsesViewPage(ListView):
    model = Course
    template_name = 'erp/courses.html'
    context_object_name = 'courses'
   



