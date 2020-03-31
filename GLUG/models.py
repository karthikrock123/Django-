from django.db import models
# Create your models here.
class Project(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    icon        = models.TextField()

class contact(models.Model):
    Phone_Number = models.TextField()
    Email_id     = models.EmailField()