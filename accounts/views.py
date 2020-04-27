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
            messages.info(request, f"You are now logged in as {username}")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")
    else:
        return render(request,"login.html")

def logout_request(request):
    auth.logout(request)
    return redirect("/")