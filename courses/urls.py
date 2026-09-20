from django.urls import path
from . import views

app_name='courses'

urlpatterns = [
    path('', views.course_display, name='course_display'),
    path('courses/', views.courses, name='courses'),
    path('course-details/', views.course_details, name='course_details'),
    path('index/', views.index, name='index'),
    path('add-course/', views.add_course, name='add_course'),
    path("details/<int:course_id>/",views.course_details,name="course_details"),
    path("edit/<int:course_id>/",views.edit_course,name="edit_course"),
    path("delete/<int:course_id>/",views.delete_course,name="delete_course"),
    
]