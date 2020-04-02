from django.shortcuts import render,redirect
from .models import Project,contact
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request,"index.html" , {'projects':projects})

def login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password  = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/") 
        else:
            messages.info(request,'User Not Found')
            return redirect("login")
    else:
        return render(request,"index.html")

def logout(request):
    auth.logout(request)
    return redirect("/")