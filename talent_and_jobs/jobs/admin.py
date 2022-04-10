from django.contrib import admin
from .models import Job,UserAppliedJob

# Register your models here.
admin.site.register(Job)
admin.site.register(UserAppliedJob)