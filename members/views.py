from django.shortcuts import render
from .models import Member
# Create your views here.

def member(request):
    members = Member.objects.all()
    return render(request,"members.html",{'members':members})