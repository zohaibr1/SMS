from django.db import models


class Student_Subject(models.Model):
    student=models.ForeignKey('app_Admin.Student', on_delete=models.CASCADE,related_name="student_subj_links")
    subject=models.ForeignKey('app_Admin.Subject', on_delete=models.CASCADE,related_name="subject_stu_links")

    def __str__(self):
        return f"{self.student}-{self.subject}"