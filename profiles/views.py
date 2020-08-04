from django.shortcuts import render, redirect, get_object_or_404
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
    else:
        return render(request, 'profiles/profile.html', {'person':request.POST['person']})

@login_required(login_url='accounts:loginuser')
def search(request):

    if request.user.type == 'tutor':
        return redirect('main:home')
    else:
        if request.method == 'GET':
            return render(request, 'profiles/search.html', {'subjects':data.subjects})
        else:
            tutor_list = []
            for tutor in TutorProfile.objects.all():
                tutor_list.append(tutor.user_id)
            client = 0
            if request.user.type == 'teacher':
                client = 1
            else:
                client = 2

            accommodations = request.POST.getlist('accommodations')
            acc = 0
            if 'ESL' in accommodations:
                acc += 1
            if 'Special Needs' in accommodations:
                acc += 2

            chosen_subjects = request.POST.getlist('subjects')

            if acc > 0:
                tutor_list = [tutor for tutor in tutor_list if
                (TutorProfile.objects.get(user_id=tutor).clients == 3 or TutorProfile.objects.get(user_id=tutor).clients == client)
                and (TutorProfile.objects.get(user_id=tutor).accommodations == acc or TutorProfile.objects.get(user_id=tutor).accommodations == 3)
                and data.common(TutorProfile.objects.get(user_id=tutor).subjects.split(', '), chosen_subjects)]


            else:
                tutor_list = [tutor for tutor in tutor_list if
                (TutorProfile.objects.get(user_id=tutor).clients == 3 or TutorProfile.objects.get(user_id=tutor).clients == client)
                and data.common(TutorProfile.objects.get(user_id=tutor).subjects.split(', '), chosen_subjects)]

            return render(request, 'profiles/results.html', {'tutors':TutorProfile.objects.all(), 'ids':tutor_list})

@login_required(login_url='accounts:loginuser')
def viewprofile(request, user_id):
    person = get_object_or_404(TutorProfile, user_id=user_id)
    return render(request, 'profiles/profile.html', {'person':person.user})

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
            if request.POST['teacher'] == 'yes':
                user.clients += 1
            if request.POST['student'] == 'yes':
                user.clients += 2
            if 'ESL' in request.POST:
                user.accommodations += 1
            if 'Special Needs' in request.POST:
                user.accommodations += 2
            user.save()
            return redirect('main:home')

    if request.user.type == 'teacher':
        if request.method == 'GET':
            return render(request, 'profiles/create.html', {'name':name, 'schools':data.teacher_schools})
        else:
            user = TeacherProfile.objects.get(user_id=request.user.id)
            user.school = request.POST['school']
            user.gradelevel = request.POST['gradelevel']
            user.save()
            return redirect('main:home')

    if request.user.type == 'student':
        if request.method == 'GET':
            return render(request, 'profiles/create.html', {'name':name, 'schools':data.schools})
        else:
            user = StudentProfile.objects.get(user_id=request.user.id)
            user.school = request.POST['school']
            user.gradelevel = request.POST['gradelevel']
            user.save()
            return redirect('main:home')

    if request.user.type == 'parent':
        if request.method == 'GET':
            return render(request, 'profiles/create.html', {'name':name, 'schools':data.schools})
        else:
            user = ParentProfile.objects.get(user_id=request.user.id)
            user.school = request.POST['school']
            user.save()
            return redirect('main:home')
