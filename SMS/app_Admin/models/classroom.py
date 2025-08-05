from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

class Classroom(models.Model):
    id=models.IntegerField(max_length=2, primary_key=True)
    name=models.CharField(max_length=50,default='class')
    def __str__(self):
        return f'{self.id}'