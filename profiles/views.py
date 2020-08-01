from django.shortcuts import render, redirect
from django.views import generic
from accounts.models import MyUser, MyUserManager
from django.contrib.auth import get_user_model
from .models import TutorProfile, StudentProfile, TeacherProfile, ParentProfile
from . import data
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:loginuser')
def profile(request):
    if request.method == 'GET':
        return render(request, 'profiles/profile.html', {'person':request.user})


def create_user(request):


    if request.user.type == 'tutor':

        profile = TutorProfile.objects.create_tutor(request.user, request.user.name)
        school = request.user.email.split('@')[1]
        profile.school = data.tutor_schools[school]
        profile.save()

        return redirect('profiles:create')

    if request.user.type == 'teacher':

        profile = TeacherProfile.objects.create_teacher(request.user, request.user.name)
        profile.save()

        return redirect('profiles:create')

    if request.user.type == 'student':

        profile = StudentProfile.objects.create_student(request.user, request.user.name)
        profile.save()

        return redirect('profiles:create')

    if request.user.type == 'parent':

        profile = ParentProfile.objects.create_parent(request.user, request.user.name)
        profile.save()

        return redirect('profiles:create')

def create(request):
    name = request.user.name.split()[0]


    if request.user.type == 'tutor':
        if request.method == 'GET':
            return render(request, 'profiles/create.html', {'name':name, 'subjects':data.subjects})
        else:
            user = TutorProfile.objects.get(user_id=request.user.id)
            chosen_subjects = request.POST.getlist('subjects')
            user.subjects = ', '.join(chosen_subjects)
            user.major = request.POST['major']
            clients = [request.POST['teacher'], request.POST['student']]
            user.clients = ', '.join(clients)
            accommodations = []
            for acc in ['ESL', 'Special Needs']:
                if acc in request.POST:
                    accommodations.append(acc)
            user.accommodations = ', '.join(accommodations)
            user.save()
            return redirect('main:home')
    if request.user.type == 'teacher':
        return render(request, 'profiles/create.html', {'name':name, 'schools':data.teacher_schools})
    if request.user.type == 'student':
        return render(request, 'profiles/create.html', {'name':name, 'schools':data.schools})
    if request.user.type == 'parent':
        return render(request, 'profiles/create.html', {'name':name, 'schools':data.schools})
