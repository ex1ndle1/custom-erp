from django.shortcuts import render
from .models import Course
# Create your views here.
from django.views.generic import DetailView,ListView
from .models import Course,Module,Subject



def index(request):
    course = Course.objects.all()
    return render(request , 'erp/index.html', {'courses':course})


class DetailViewPage(DetailView):
    model = Course
    template_name = 'erp/detail.html'
    context_object_name = 'course'
    pk_url_kwarg = 'course_id'
   
     
    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        context['modules'] = Module.objects.all()
        context['subjects'] = Subject.objects.all()
        return  context
    


class CorsesViewPage(ListView):
    model = Course
    template_name = 'erp/courses.html'
    context_object_name = 'courses'
   

class SubjectViewPage(DetailView):
     template_name  = 'erp/subject.html'
     model = Subject
     pk_url_kwarg = 'subject_id'
     context_object_name = 'subject'

