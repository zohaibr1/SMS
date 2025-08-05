from django.db import models
from django.contrib.auth.models import User 
from .school import School
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id=models.CharField(max_length=50, unique=True, primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    subject=models.ManyToManyField('app_Admin.Subject', through='Teacher_Subject', related_name='subject_of_teachers')
    classroom=models.ManyToManyField('app_Admin.classroom', through='Teacher_Classroom', related_name='classroom_of_teachers')
    address=models.TextField()
    contact_no=models.CharField(max_length=11)
    email=models.EmailField(unique=True)
    Join_date=models.DateField()
    school=models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} - {self.id}' 
    