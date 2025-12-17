from django.contrib import admin
from .models import Course, Subject,Teacher, Module
# Register your models here.

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Subject)
admin.site.register(Teacher)
