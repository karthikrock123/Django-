from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
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
    return render(request,"project_page.html")