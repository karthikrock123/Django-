from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.db.models.query import QuerySet
from .models import listOfProject
from GLUG.models import Project
# Create your views here.

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("project_page")
        else:
            messages.error(request, "Invalid user")
            return redirect("login")
    else:
        return render(request,"login.html")

def logout_request(request):
    auth.logout(request)
    return redirect("/")

def project_request(request):
    pop=[];cs=[];ps=[]
    if User.is_authenticated: 
        a = request.user.id 
        if(listOfProject.objects.filter(name_id=a)):
            u = listOfProject.objects.filter(name = a)
            us = u.values('projects')
            #print(us)
            for i in us:
                pop.append(i)
            #print(pop)
            for i in range(0,len(pop)):
                x = (pop[i].get('projects'))
                cs.append(x)
            #print(cs)
            for i in cs:
                p = Project.objects.filter(id = i)
                ps.append(p.values('name'))
            print(ps)
        return render(request,"Project_page.html",{'ps':ps})
    