from django.contrib import admin
from .models import Project,contact

# Register your models here.
class GLUGview(admin.ModelAdmin):
    
    list_display = ['name','Email_id','Phone_Number']
    search_fields = ['name']

class GLUGview1(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Project,GLUGview1)
admin.site.register(contact,GLUGview)