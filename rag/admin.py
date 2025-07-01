from django.contrib import admin
from .models import Courses, CourseContent

# Register your models here.

admin.site.register(Courses)
admin.site.register(CourseContent)