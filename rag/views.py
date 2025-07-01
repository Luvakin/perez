from django.shortcuts import render
from .models import Courses, CourseContent
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.


def index(request):
    Course_new = Courses.objects.all()
    Course_content = CourseContent.objects.all()
    context = {
        'Courses': Course_new,
        'coursecontent': Course_content,
    }
    return render(request, 'rag/index.html', context)

    

def llm(request):
    return render(request, 'rag/llm.html', {})



# def add_course(request):
#     if request.method == 'POST':
#         courseName = request.POST.get('courseName')
#         courseCode = request.POST.get('courseCode')
#         instructor = request.POST.get('instructor')
#         description = request.POST.get('courseColor')

#         courses = Courses.objects.create(
#             course_name = courseName,
#             course_codr = courseCode,
#             instructor = instructor,
#             description = description
#         )

        


#     return render(request, 'rag/index.html',)







@require_POST
def create_course(request):
    name = request.POST.get('courseName')
    code = request.POST.get('courseCode')
    instructor = request.POST.get('instructor') or None
    description = request.POST.get('description') or None

    if name and code:
        if Courses.objects.filter(course_name=name).exists():
            messages.error(request, "A course with this name already exists.")
        elif Courses.objects.filter(course_code=code).exists():
            messages.error(request, "A course with this code already exists.")
        else:
            Courses.objects.create(
                course_name=name,
                course_code=code,
                instructor=instructor,
                description=description
            )
            messages.success(request, "Course created successfully.")
            print("Course created successfully:", name, code, instructor, description)
    else:
        messages.error(request, "Please fill in all required fields.")
        print("Failed to create course: Missing required fields.")

    return redirect('rag:index')  # Redirect to the index page after creating the course