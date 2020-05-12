from django.db import models
from django.contrib.auth.models import User
from GLUG.models import Project

# Create your models here.
class listOfProject(models.Model):
    name     = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    projects = models.ManyToManyField(Project)



class Milestone(models.Model):
    name       = models.ForeignKey(Project,null=True,on_delete=models.SET_NULL)
    goals      = models.TextField(blank=True)
    completed  = models.BooleanField(default=False)






# class Milestones(models.Model):
#     project          =   models.ForeignKey(Project,null=True,on_delete=models.SET_NULL)
#     comments         =   models.ManyToOneRel(MilestoneObjects,on_delete=models.SET_NULL)
