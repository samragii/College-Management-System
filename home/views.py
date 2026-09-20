from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def homepage(request):
    return render(request, 'home/home.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')



@login_required
def profile_create(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'home/profile.html', {
        'form': form,
    })
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from students.models import Student
from teachers.models import Teacher
from courses.models import Course


def is_admin(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        "student_count": Student.objects.count(),
        "active_student_count": Student.objects.filter(status="active").count(),

        "teacher_count": Teacher.objects.count(),
        "active_teacher_count": Teacher.objects.filter(status="active").count(),

        "course_count": Course.objects.count(),
        "active_course_count": Course.objects.filter(status="active").count(),

        "recent_students": Student.objects.order_by("-id")[:5],
        "recent_teachers": Teacher.objects.order_by("-id")[:5],
        "recent_courses": Course.objects.order_by("-id")[:5],
    }

    return render(request, "home/admin_dashboard.html", context)