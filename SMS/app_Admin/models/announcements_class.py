from django.db import models

class announcement_class(models.Model):
    announcement = models.ForeignKey( 'app_Admin.Announcement',on_delete=models.CASCADE,related_name='announcement_links')
    classroom = models.ForeignKey(  'app_Admin.Classroom',  on_delete=models.CASCADE, related_name='announcment_classroom_links')

    def __str__(self):
        return f"{self.announcement} - {self.classroom}"