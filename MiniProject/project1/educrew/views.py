from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import *
from .filters import *
from .forms import *
#from .decorators import restricted_users

#@restricted_users('Admin')
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user=authenticate(request,username=username,password= password)
            if user is not None :
                login(request, user)
                return redirect('home') 
            else:
                messages.info(request,'Username/Password is incorrect')
        context = {}
        return render(request,'educrew/login.html',context)
    context = {}
    return render(request,'educrew/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    #date and time info
    today = datetime.now()
    date = today.strftime("%d %B, %Y")
    day = today.strftime("%A")

    #user info
    role = str(request.user.groups.values_list('name', flat=True).first())
    person = request.user.username
    if(role == 'Student'):
        user = Student.objects.get(rollno=person)

        #schedule info
        yr = user.year
        dept_id = user.dept_id
        section = user.sec
        schedule = StudentSchedule.objects.get(dept_id=dept_id,year=yr,sec=section,day=day)
        if schedule.p1 is None: p1 = "Free" 
        else: p1 = SubjectInfo.objects.get(unq_id=schedule.p1)
        if schedule.p2 is None: p2 = "Free" 
        else: p2 = SubjectInfo.objects.get(unq_id=schedule.p2)
        if schedule.p3 is None: p3 = "Free" 
        else: p3 = SubjectInfo.objects.get(unq_id=schedule.p3)
        if schedule.p4 is None: p4 = "Free" 
        else: p4 = SubjectInfo.objects.get(unq_id=schedule.p4)


        #Announcements
        date2 = today.strftime("%Y-%m-%d")
        annc = Announcements.objects.filter(dept_id=dept_id,year=yr,sec=section,date=date2) 
        count = annc.count

        context = {'user':user, 'date':date, 'day': day,
        'schedule':schedule,
        'role' : role,'cond':True,'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4,
        'announcements': annc,'free':"Free",'count':count,
        }
    elif(role == 'Faculty'):
        user = Lecturer.objects.get(lect_id=person)
        #schedule info
        schedule = LecturerSchedule.objects.get(lect_id=person,day=day)
        if schedule.p1 is None: p1 = "Leisure" 
        else: p1 = SubjectInfo.objects.get(unq_id=schedule.p1)
        if schedule.p2 is None: p2 = "Leisure" 
        else: p2 = SubjectInfo.objects.get(unq_id=schedule.p2)
        if schedule.p3 is None: p3 = "Leisure" 
        else: p3 = SubjectInfo.objects.get(unq_id=schedule.p3)
        if schedule.p4 is None: p4 = "Leisure" 
        else: p4 = SubjectInfo.objects.get(unq_id=schedule.p4)
        

        context = {'user':user, 'date':date, 'day': day,
        'schedule':schedule,
        'role' : role,'cond':False,'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4,
        'leisure':"Leisure",
        }
    else:
        messages.info(request,'Your role is not specified! Cannot Authenticate')
        logout(request)
        return redirect('login')

    return render(request,'educrew/home.html',context)

@login_required(login_url='login')
def profile(request):
    role = str(request.user.groups.values_list('name', flat=True).first())
    person = request.user.username
    if(role == 'Student'):
        user = Student.objects.get(rollno=person)
        context = {'user':user,'role' : role, 'cond':True,}
    if(role == 'Faculty'):
        user = Lecturer.objects.get(lect_id=person)
        context = {'user':user,'role' : role, 'cond':False,}

    
    return render(request,'educrew/profile.html',context)

@login_required(login_url='login')
def exploreStudents(request):
    students = Student.objects.all()    
    sfilter = StudentFilter(request.GET, queryset=students)
    students = sfilter.qs

    context = {'students':students, 'sfilter':sfilter,}
    return render(request,'educrew/exploreStudents.html',context)

@login_required(login_url='login')
def exploreFaculty(request):
    lecturers = Lecturer.objects.all()
    lfilter = LecturerFilter(request.GET, queryset=lecturers)
    lecturers = lfilter.qs

    context = {'lecturers':lecturers, 'lfilter':lfilter,}
    return render(request,'educrew/exploreFaculty.html',context)

@login_required(login_url='login')
def announcement(request):
    user = request.user
    lect_id = request.user.username
    lect = Lecturer.objects.get(lect_id=lect_id)
    form = AnnounceForm(instance=user)

    context= {'form':form,'lect':lect}
    return render(request,'educrew/announcement.html',context)

@login_required(login_url='login')
def makeAnnouncement(request):
    user = request.user
    lect_id = request.user.username
    lect = Lecturer.objects.get(lect_id=lect_id)

    if request.method == 'GET':
        k = request.GET
        year = k.get("year", "0")
        dept_id = k.get("dept_id", "0")
        sec = k.get("sec", "0")
        date = k.get("date", "0")
        note = k.get("note", "0")

        dept = Dept.objects.get(dept_id=dept_id)

        a = Announcements(lect_id=lect,year=year,dept_id=dept,sec=sec,date=date,note=note)
        a.save()
        return redirect('home')

@login_required(login_url='login')
def viewFaculty(request,pk):
    user = Lecturer.objects.get(lect_id=pk)

    today = datetime.now()
    day = today.strftime("%A")

    #schedule info
    schedule = LecturerSchedule.objects.get(lect_id=pk,day=day)
    if schedule.p1 is None: p1 = "Leisure" 
    else: p1 = SubjectInfo.objects.get(unq_id=schedule.p1)
    if schedule.p2 is None: p2 = "Leisure" 
    else: p2 = SubjectInfo.objects.get(unq_id=schedule.p2)
    if schedule.p3 is None: p3 = "Leisure" 
    else: p3 = SubjectInfo.objects.get(unq_id=schedule.p3)
    if schedule.p4 is None: p4 = "Leisure" 
    else: p4 = SubjectInfo.objects.get(unq_id=schedule.p4)
    

    context = {'user':user, 'schedule':schedule,'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4,
    'leisure':"Leisure",
    }
    return render(request,'educrew/viewFaculty.html',context)

@login_required(login_url='login')
def viewStudent(request,pk):
    user = Student.objects.get(rollno=pk)

    today = datetime.now()
    day = today.strftime("%A")

    yr = user.year
    dept_id = user.dept_id
    section = user.sec

    #schedule info
    schedule = StudentSchedule.objects.get(dept_id=dept_id,year=yr,sec=section,day=day)
    if schedule.p1 is None: p1 = "Free" 
    else: p1 = SubjectInfo.objects.get(unq_id=schedule.p1)
    if schedule.p2 is None: p2 = "Free" 
    else: p2 = SubjectInfo.objects.get(unq_id=schedule.p2)
    if schedule.p3 is None: p3 = "Free" 
    else: p3 = SubjectInfo.objects.get(unq_id=schedule.p3)
    if schedule.p4 is None: p4 = "Free" 
    else: p4 = SubjectInfo.objects.get(unq_id=schedule.p4)
    

    context = {'user':user, 'schedule':schedule,'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4,
    'free':"Free",
    }
    return render(request,'educrew/viewStudent.html',context)


def search(request):
    context = {    }
    return render(request,'educrew/viewStudent.html',context)