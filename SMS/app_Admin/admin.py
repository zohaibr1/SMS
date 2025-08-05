from django.contrib import admin
from app_Admin.models import School,Student,Teacher,Subject, Classroom,Attendance
# Register your models here.
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Attendance)
admin.site.register(School)
