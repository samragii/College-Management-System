from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
from django.shortcuts import render
from datetime import datetime


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
@login_required
def students_home(request):
    return render(request, 'home.html')
@login_required
def students_about(request):
    return render(request, 'about.html')


students = [{
        "student_id": 1,
        "name": "Kaushal Karn",
        "age": 20,
        "grade": "A",
        "course": "Computer Science"
    },
                {
        "student_id": 2,
        "name": "John Doe",
        "age": 22,
        "grade": "B",
        "course": "Mathematics"
    },
                {
        "student_id": 3,
        "name": "harry Potter",
        "age": 20,
        "grade": "A",
        "course": "Computer Science"
    }
        ,        {
        "student_id": 4,
        "name": "Jane Smith",
        "age": 19,
        "grade": "B",
        "course": "Physics"
    }
    ]

def student_display(request):
    # stu = dict(students)
    return JsonResponse(students, safe=False)

def student_details(request, student_id):
    for student in students:
        if student["student_id"] == student_id:
            return JsonResponse(student)
           
            # return HttpResponse(student)    
    return HttpResponse("Student not found.")

@login_required
def student_list(request):
    students = Student.objects.all()
    context={
        "students":students
    }
    return render(request,'students/student_list.html',context)
     
def index(request):
    return render(request, 'students/index.html')

def student_detail(request):
    return render(request, 'students/student_details.html')

@login_required
def add_students(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        Student.objects.create(
            student_id=request.POST.get("student_id"),
            first_name=first_name,
            last_name=last_name,
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date_of_birth=request.POST.get("date_of_birth"),
            department=request.POST.get("department"),
            program=request.POST.get("program"),
            semester=request.POST.get("semester"),
            batch=request.POST.get("batch"),
            status=request.POST.get("status"),
            address=request.POST.get("address"),
            notes=request.POST.get("notes"),
        )
        messages.success(
       request,
    f"Student {first_name} {last_name} registered successfully!"
       )

    return render(request, "students/add_student.html")

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.student_id = request.POST.get("student_id")
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.department = request.POST.get("department")
        student.program = request.POST.get("program")
        student.semester = request.POST.get("semester")
        student.batch = request.POST.get("batch")
        student.status = request.POST.get("status")
        student.address = request.POST.get("address")
        student.notes = request.POST.get("notes")

        student.save()

        return redirect("students:student_list")

    return render(
        request,
        "students/edit_student.html",
        {"student": student}
    )

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()

    return redirect("students:student_list")

from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
      model = Student
      template_name = 'students/student_list_cbv.html'
      context_object_name = 'students'
      ordering = ['first_name']
      paginate_by = 10

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Student

class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Student

    fields = [
        'first_name',
        'last_name',
        'student_id',
        'email',
        'phone',
        'date_of_birth',
        'department',
        'semester',
        'batch',
        'program',
        'status',
        'address',
        'notes'
    ]

    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')

    def test_func(self):
        return self.request.user.groups.filter(
            name="Teacher"
        ).exists()
        
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_lists(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)