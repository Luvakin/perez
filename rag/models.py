from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Courses (models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_code = models.CharField(max_length=10, unique=True)
    instructor = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug  = models.SlugField(default='', null=False)


    class Meta:
        verbose_name_plural = 'Courses'



    def __str__(self):
        return self.course_name 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super().save(*args, **kwargs)
        



class CourseContent(models.Model):   
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='contents')
    type = models.CharField(max_length=50, choices=[('text', 'Text'), ('video', 'Video'), ('image', 'Image')])
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='course_content_files/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default='', null=False)




    class Meta:
        verbose_name_plural = 'Course Contents'
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} ({self.type}) - {self.course.course_name}"
    


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
