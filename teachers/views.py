from django.shortcuts import render,redirect
from .models import Teacher
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
@login_required
def teachers_list(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers
    }

    return render(request, 'teachers/teacher_list.html', context)
@login_required
def teachers_detail(request,teacher_id):
    return render(request, 'teachers/teacher_detail.html')
@login_required
def teachers_home(request):
    return render(request, 'teachers/home.html')
@login_required
def index(request):
    teachers_list =Teacher.objects.all()
    active_teacher=teachers_list.filter(status='active')
    inactive_teacher=teachers_list.filter(status='inactive')
    departments = Teacher.objects.values('department').distinct()
   
    context = {
            'teachers':teachers_list,
            'total_teacher': teachers_list.count(),
            'active_teacher': active_teacher.count(),
            'inactive_teacher': inactive_teacher.count(),
            'departments':len(departments),
   
        }
    return render(request, 'teachers/index.html')
@login_required
def add_teachers(request):
    if request.method == "POST":
        Teacher.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            department=request.POST.get("department"),
            position=request.POST.get("position"),
            qualification=request.POST.get("qualification"),
            experience=request.POST.get("experience"),
            joining_date=request.POST.get("joining_date"),
            status=request.POST.get("status"),
            bio=request.POST.get("bio"),
        )

        return redirect('teachers:teachers')

    return render(request, 'teachers/add_teacher.html')

@login_required
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == "POST":
        teacher.first_name = request.POST.get("first_name")
        teacher.last_name = request.POST.get("last_name")
        teacher.email = request.POST.get("email")
        teacher.phone = request.POST.get("phone")
        teacher.department = request.POST.get("department")
        teacher.position = request.POST.get("position")
        teacher.qualification = request.POST.get("qualification")
        teacher.experience = request.POST.get("experience")
        teacher.joining_date = request.POST.get("joining_date")
        teacher.status = request.POST.get("status")
        teacher.bio = request.POST.get("bio")

        teacher.save()

        return redirect("teachers:teachers")

    return render(
        request,
        "teachers/edit_teacher.html",
        {"teacher": teacher}
    )


@login_required
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == "POST":
        teacher.delete()

    return redirect("teachers:teachers")

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeacherSerializer

@api_view(['GET', 'POST'])
def teacher_lists(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)