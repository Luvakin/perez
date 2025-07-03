from django.contrib import admin
from .models import Courses, CourseContent

# Register your models here.
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'instructor', 'description')
    search_fields = ('course_name', 'course_code', 'instructor')
    prepopulated_fields = {'slug': ('course_name',)}




class CourseContentAdmin(admin.ModelAdmin):
    list_display = ('course', 'type', 'title', 'date')
    search_fields = ('course__course_name', 'title')
    list_filter = ('type', 'date')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Courses, CoursesAdmin)
admin.site.register(CourseContent, CourseContentAdmin)