from django.views                       import View
from django.shortcuts                   import render, redirect, get_object_or_404
from django.http                        import HttpResponse, JsonResponse
from django.contrib.auth.models         import User
from django.contrib.auth                import authenticate, login as auth_login
from django.contrib.auth.views          import LoginView
from app_Admin.forms.teacher_form       import TeacherForm
from app_Admin.forms.announcementform   import AnnouncementForm
from app_Admin.forms.student_form       import StudentForm
from django.contrib                     import messages
from app_Admin.models                   import Teacher, Student,Classroom, Attendance, Announcement, Subject
from django.contrib.auth.decorators     import login_required
from datetime                           import datetime
from django.core.exceptions             import ValidationError
from django.views.decorators.http       import require_POST
from datetime                           import date
from django.utils                       import timezone

#dashboard of student
class studentDashboard(View):
    def get(self,request):
        user = request.user
        try:
           student = Student.objects.select_related('classroom').prefetch_related('subject').get(user=user)
        except Student.DoesNotExist:
            student = None

        attendance_records = Attendance.objects.filter(student=student).order_by('-date')[:5]  # last 5 records
        announcements = Announcement.objects.all().order_by('-created_at')[:5]
        
        subjects = student.subject.all() if student else []
        teachers = Teacher.objects.filter(subject__in=subjects).distinct() if student else []


        context = {
            'student': student,
            'subjects': subjects,
            'teachers': teachers,
            'attendance_records': attendance_records,
            'announcements': announcements,
        }

        return render(request, 'dashboard_students.html', context)
    
#Announcement View
class announcementView(View):
    def get(self,request):
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:
            return JsonResponse({'error':'Error'},status=400)
        announcements = []
        if student:
            classrooms = [student.classroom]
            subjects = student.subject.all() if student else []  
            assigned_teachers = Teacher.objects.filter(subject__in=subjects).distinct() if student else []
            announcements = Announcement.objects.filter(tragetClass=student.classroom,uploader__in=assigned_teachers ).order_by('-created_at')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = []
            for announcement in announcements:
                data.append({
                    'title': announcement.title,
                    'content': announcement.content,
                    'created_at': announcement.created_at.strftime("%b %d, %Y %H:%M"),
                    'uploader': f"{announcement.uploader.first_name} {announcement.uploader.last_name}"
                })
            return JsonResponse({'announcements': data}, status=200)
        return render(request, 's_announcements.html', {
        'announcements': announcements
        })
    
#Atendance view students
class anttendanceView(View):
    def get(self,request):
        user=request.user
        try:
                student=Student.objects.get(user=user)
        except Student.DoesNotExist:
            return JsonResponse({'error':'Error'},status=400)
        attendance_records = Attendance.objects.filter(student=student).order_by("-date")
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            print(f"Attendance records found: {len(attendance_records)}")
            data = [
                {
                    'date': record.date.strftime('%Y-%m-%d'),
                    'teacher': str(record.teacher),
                    'attendance': record.attendance
                }
                for record in attendance_records
            ]
            print("JSON response:", data)
            return JsonResponse({'records': data})

        # Return template for normal page load
        
        return render(request, 's_Attendance.html',{'attendance_records': attendance_records})
    