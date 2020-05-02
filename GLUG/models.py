from django.db import models
# Create your models here.
class Project(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    icon        = models.TextField()

    def __str__(self):
        return self.name

class contact(models.Model):
    name         = models.CharField(max_length=100)
    Phone_Number = models.TextField()
    Email_id     = models.EmailField()

    def __str__(self):
        return self.name