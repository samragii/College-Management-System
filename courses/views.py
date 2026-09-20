from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Course
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer

@login_required
def course_display(request):
    return HttpResponse("This is the course display page.")
@login_required
def courses(request):
    courses_list = Course.objects.all()

    context = {
        "courses": courses_list}
   
    return render(request, 'courses/courses.html', context)
@login_required
def course_details(request, course_id):
    course = Course.objects.get(id=course_id)

    return render(
        request,
        "courses/course_details.html",
        {"course": course}
    )

@login_required
def edit_course(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id
    )

    courses = Course.objects.filter(
        status="active"
    )

    if request.method == "POST":

        course.code = request.POST.get("code")
        course.name = request.POST.get("name")
        course.department = request.POST.get("department")
        course.instructor_id = request.POST.get("instructor")
        course.credits = request.POST.get("credits")
        course.duration = request.POST.get("duration")
        course.semester = request.POST.get("semester")
        course.capacity = request.POST.get("capacity")
        course.status = request.POST.get("status")
        course.description = request.POST.get("description")

        course.save()

        return redirect("courses:courses")

    context = {
        "course": course,
        "courses": courses,
    }

    return render(
        request,
        "courses/edit_course.html",
        context
    )

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    course.delete()

    return redirect("courses:courses")

@login_required
def index(request):
    courses_list = Course.objects.all()

    active_course = courses_list.filter(status="active")
    inactive_course = courses_list.filter(status="inactive")

    departments = (
        Course.objects
        .values_list("department", flat=True)
        .distinct()
        .order_by("department")
    )

    context = {
        "courses": courses_list,
        "total_course": courses_list.count(),
        "active_course": active_course.count(),
        "inactive_course": inactive_course.count(),
        "departments": len(departments),
    }

    return render(
        request,
        "courses/index.html",
        context
    )

@login_required
def add_course(request):
    courses = Course.objects.filter(status="active")

    if request.method == "POST":
        Course.objects.create(
            code=request.POST.get("code"),
            name=request.POST.get("name"),
            department=request.POST.get("department"),
            instructor_id=request.POST.get("instructor"),
            credits=request.POST.get("credits"),
            duration=request.POST.get("duration"),
            semester=request.POST.get("semester"),
            capacity=request.POST.get("capacity"),
            status=request.POST.get("status"),
            description=request.POST.get("description"),
        )
        return redirect('courses:courses')

    return render(
        request,
        "courses/add-course.html",
        {"courses": courses}
    )
@api_view(['GET', 'POST'])
def course_lists(request):

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )