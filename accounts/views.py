from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
from home.models import Profile


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home:home_page')

    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Create profile
            Profile.objects.create(user=user)

            # Automatically make new users Students
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)

            # Log the user in
            login(request, user)

            return redirect('home:home_page')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })