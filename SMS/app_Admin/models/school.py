from django.db import models
#Create your models here.

#School Model
class School(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name=models.CharField(max_length=50, default='The Sky-infinit School ')
    
    def __str__(self):
        return f"{self.name}"