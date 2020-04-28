from django.contrib import admin
from .models import Member
# Register your models here.
class GLUGview(admin.ModelAdmin):

    list_display  = ['name','pin_no','designation']
    search_fields = ['name']

admin.site.register(Member,GLUGview)