from django.db import models
from django.contrib.auth.models import User
from GLUG.models import Project 

# Create your models here.
class listOfProject(models.Model):
    name     = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    projects = models.ManyToManyField(Project)
