from django.urls import path
from . import views

app_name = 'rag'

urlpatterns = [
   
    
    path('', views.redirect_to_first_course, name='home_redirect'),
    path('create_course/',views.create_course, name="add_courses"),
    path('llm/', views.llm, name='llm'),
    path('<slug:slug>/', views.index, name='index'),
    
    
]
