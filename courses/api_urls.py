from django.urls import path
from . import views

app_name = 'courses_api'

urlpatterns = [
    path('course-lists/', views.course_lists, name='course_lists'),
]