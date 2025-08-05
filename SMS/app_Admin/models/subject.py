from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from .classroom import Classroom
class Subject(models.Model):
    id=models.CharField(max_length=50, primary_key=True)
    name=models.CharField(max_length=50,)
    classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE, default='9')   
    def __str__(self):
        return f'{self.name}{self.id}'