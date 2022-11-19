from django.contrib import admin

# Register your models here.
from .models import Student
#add student to admin site
admin.site.register(Student)
