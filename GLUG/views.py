from django.shortcuts import render
from .models import Project,contact
# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request,"index.html" , {'projects':projects})