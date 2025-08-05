from django.shortcuts               import render
from .views_part.login_view         import loginView
from .views_part.logout_view        import logoutView
from .views_part.admin_view          import addNewStudents,listOfStudents,editStudents,deleteStudents,          addNewTeachers,editTeachers,listOfTeachers,deleteTeacher
from .views_part.teacher_view       import teacherDashboardView,AssignStudents,markAttendance,deleteAnnouncemment,makeAnnouncemeent
from .views_part.student_view       import studentDashboard,announcementView,anttendanceView




# Create your views here.      
#school admin panel 
def school(request):
    return render(request,'school.html')
