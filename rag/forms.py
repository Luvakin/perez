from django import forms
from .models import Courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['course_name', 'course_code', 'instructor', 'description']
        widgets = {
            'course_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-[#d4dbe2] rounded-xl focus:outline-none focus:ring-2 focus:ring-[#dce7f3] focus:border-transparent text-[#101418] text-sm',
                'id': 'courseName',
                'placeholder': 'Enter course name',
            }),
            'course_code': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-[#d4dbe2] rounded-xl '
                         'focus:outline-none focus:ring-2 focus:ring-[#dce7f3] '
                         'focus:border-transparent text-[#101418] text-sm',
                'id': 'courseCode',
                'placeholder': 'e.g., PSYC 101',
            }),
            'instructor': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-[#d4dbe2] rounded-xl '
                         'focus:outline-none focus:ring-2 focus:ring-[#dce7f3] '
                         'focus:border-transparent text-[#101418] text-sm',
                'id': 'instructor',
                'placeholder': 'Enter instructor name(s)',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-[#d4dbe2] rounded-xl '
                         'focus:outline-none focus:ring-2 focus:ring-[#dce7f3] '
                         'focus:border-transparent text-[#101418] text-sm resize-none',
                'id': 'description',
                'placeholder': 'Enter course description',
                'rows': '3',
            }),
        }
