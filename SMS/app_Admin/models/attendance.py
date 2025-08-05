from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from .subject import Subject
from .student import Student
from .teacher import Teacher


class Attendance(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    date=models.DateField()
    attendance=models.CharField(choices=[('PRESENT','present'),('ABSENT','absent'),('LEAVE','leave')])
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
