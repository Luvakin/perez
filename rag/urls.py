from django.urls import path
from . import views

app_name = 'rag'

urlpatterns = [
    path('', views.index, name='index'),
    path('llm/', views.llm, name='llm'),
    path('create_course/',views.create_course, name="add_courses")
]
