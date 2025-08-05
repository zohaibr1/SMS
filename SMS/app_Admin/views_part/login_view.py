from django.views import View
from django.shortcuts               import render, redirect, get_object_or_404
from django.http                    import HttpResponse
from django.contrib.auth.models     import User
from django.contrib.auth            import authenticate, login as auth_login
from django.contrib.auth.views      import LoginView
from app_Admin.forms.teacher_form       import TeacherForm
from app_Admin.forms.announcementform   import AnnouncementForm
from app_Admin.forms.student_form       import StudentForm

from django.contrib                 import messages
from app_Admin.models               import Teacher,Student,Classroom,Subject,Attendance,Announcement
from django.contrib.auth.decorators import login_required
from datetime                       import datetime
from django.core.exceptions         import ValidationError
from django.views.decorators.http   import require_POST
from datetime                       import date
from django.utils                   import timezone

class loginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)

            if user.is_superuser: 
                return redirect('/school/')  # redirect to Django admin

            elif hasattr(user, 'teacher'):
                return redirect('dashboard_teachers')

            elif hasattr(user, 'student'):
                return redirect('dashboard_students')

            else:
                return render(request, 'login.html', {'error': 'User has no role assigned'})

        return render(request, 'login.html', {'error': 'Invalid credentials'})