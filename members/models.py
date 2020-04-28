from django.db import models
# Create your models here.
class Member(models.Model):
    name        = models.CharField(max_length=100)
    img         = models.ImageField(upload_to ='pics' )
    pin_no      = models.TextField()
    designation = models.TextField()

    def __str__(self):
        return self.name
