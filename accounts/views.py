from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, views, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser
from django.db import IntegrityError
from profiles.models import TutorProfile, StudentProfile

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupuser.html')
    else:
        pass

def tutor(request):

    schools = {
        '@oakland.edu':'Oakland University',
        '@umich.edu':'University of Michigan Ann Arbor',
    }

    if request.method == 'GET':
        return render(request, 'accounts/signuptutor.html', {'schools':schools.keys()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            email = request.POST['username'] + request.POST['school']
            try:
                user = MyUser.objects.create_user(
                    email,
                    request.POST['date_of_birth'],
                    request.POST['name'],
                    'tutor',
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('profiles:create_user')
            except IntegrityError:
                return render(request, 'accounts/signuptutor.html', {'error':'Email is already in use', 'schools':schools.keys()})
        else:
            return render(request, 'accounts/signuptutor.html', {'error':'Passwords did not match', 'schools':schools.keys()})

def teacher(request):

    schools = [
        '@uticak12.org',
    ]

    if request.method == 'GET':
        return render(request, 'accounts/signuptutor.html', {'schools':schools})
    else:
        if request.POST['password1'] == request.POST['password2']:
            email = request.POST['username'] + request.POST['school']
            try:
                user = MyUser.objects.create_user(
                    email,
                    request.POST['date_of_birth'],
                    request.POST['name'],
                    'teacher',
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('profiles:create_user')
            except IntegrityError:
                return render(request, 'accounts/signuptutor.html', {'error':'Email is already in use', 'schools':schools})
        else:
            return render(request, 'accounts/signuptutor.html', {'error':'Passwords did not match', 'schools':schools})

def student(request):
        if request.method == 'GET':
            return render(request, 'accounts/signupparent.html')
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = MyUser.objects.create_user(
                        request.POST['username'],
                        request.POST['date_of_birth'],
                        request.POST['name'],
                        'student',
                        password=request.POST['password1']
                    )
                    user.save()
                    login(request, user)
                    return redirect('profiles:create_user')
                except IntegrityError:
                    return render(request, 'accounts/signupparent.html', {'error':'Email is already in use'})
            else:
                return render(request, 'accounts/signupparent.html', {'error':'Passwords did not match'})

def parent(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupparent.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = MyUser.objects.create_user(
                    request.POST['username'],
                    request.POST['date_of_birth'],
                    request.POST['name'],
                    'parent',
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('profiles:create_user')
            except IntegrityError:
                return render(request, 'accounts/signupparent.html', {'error':'Email is already in use'})
        else:
            return render(request, 'accounts/signupparent.html', {'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password do not match'})
        else:
            login(request, user)
            return redirect('main:home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main:home')
