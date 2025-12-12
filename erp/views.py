from django.shortcuts import render
from .models import Course
# Create your views here.


def index(request):
    course = Course.objects.all()
    return render(request , 'erp/index.html', {'courses':course})