from django.db import models
class Teacher_classroom(models.Model):
    teacher=models.ForeignKey('app_Admin.Teacher',on_delete=models.CASCADE,related_name='teacher_classroom_links')
    classroom=models.ForeignKey('app_Admin.Classroom',on_delete=models.CASCADE,related_name='classroom_teacher_links')

    def __str__(self):
            return f"{self.teacher}-{self.classroom}"