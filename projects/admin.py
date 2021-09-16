from django.contrib import admin

# Register your models here.
from .models import General_info, Project, Jobs

admin.site.register(General_info)
admin.site.register(Project)
admin.site.register(Jobs)