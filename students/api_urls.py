from django.urls import path
from . import views
from .views import StudentListView,StudentCreateView

app_name='students_api'

urlpatterns = [
 
    path('student-lists/', views.student_lists, name='student_lists'),

]