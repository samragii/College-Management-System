from django.urls import path
from .import views

app_name='teachers'

urlpatterns = [
      path('index/', views.index, name='index'),
      path('teacher-list/', views.teachers_list, name='teachers'),
      path('teacher/', views.teachers_detail, name='teacher_detail'),
      path('add-teacher/', views.add_teachers,name='add_teacher'),
      path('edit-teacher/<int:teacher_id>/', views.edit_teacher,name='edit_teacher'),
      path('delete-teacher/<int:teacher_id>/', views.delete_teacher,name='delete_teacher'),
      path('teacher-lists/', views.teacher_lists, name='teacher_lists'),

]
