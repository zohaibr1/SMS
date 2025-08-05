from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from .subject import Subject
from .teacher import Teacher
from .announcements_class import announcement_class

class Announcement(models.Model):
    title=models.CharField( max_length=200)
    content=models.TextField()
    uploader=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tragetClass = models.ManyToManyField('app_Admin.Classroom', through='announcement_class', related_name='announcement_targets')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title