from django.db import models
class Teacher_Subject(models.Model):
    teacher=models.ForeignKey('app_Admin.Teacher',on_delete=models.CASCADE,related_name='teacher_sub_links')
    subject=models.ForeignKey('app_Admin.Subject',on_delete=models.CASCADE,related_name='subject_teach_links')

    def __str__(self):
            return f"{self.teacher}-{self.classroom}"