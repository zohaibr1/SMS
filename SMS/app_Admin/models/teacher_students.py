from django.db import models

class Teacher_Students(models.Model):
    teacher=models.ForeignKey('app_Admin.Teacher', on_delete=models.CASCADE, related_name="teacher_stu_links")
    student=models.ForeignKey('app_Admin.Student', on_delete=models.CASCADE, related_name="student_teach_links")
    def __str__(self):
        return f"{self.teacher}-{self.student}" 