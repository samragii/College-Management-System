from django.urls import path
from . import views
from .views import StudentListView,StudentCreateView

app_name='students'

urlpatterns = [
 
    path('student-list/', views.student_list, name='student_list'),
    path('index/', views.index, name='index'),
    path('student/', views.student_detail, name='student_details'),
    path('add-students/', views.add_students, name='add_students'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('student_list_view/',StudentListView.as_view(), name='student_view'),
    path('add/', StudentCreateView.as_view(), name='student_create'),
    path('student-lists/', views.student_lists, name='student_lists'),
]