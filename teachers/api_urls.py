from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('teacher-lists/', views.teacher_lists, name='teacher_lists'),
]