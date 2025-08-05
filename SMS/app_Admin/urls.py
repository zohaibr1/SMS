from django.contrib import admin
from django.urls import path
from . import views_part, views
# from app_Admin.views_part.ajax_filter_students_view import ajax_filter_students
from app_Admin.views_part.login_view import loginView
from app_Admin.views_part.logout_view import logoutView
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/', permanent=True)),
    path('login/',loginView.as_view(), name='login'),
    path('logout/',logoutView.as_view(), name='logout'),
    path('school/',views.school, name='school'),
    path('add_students/',views.addNewStudents.as_view(), name='add_students'),
    path('list_students/',views.listOfStudents.as_view(), name='list_students'),
    path('edit_students/<str:student_id>/',views.editStudents.as_view(), name='edit_students'),
    path('delete_students/<str:student_id>/', views.deleteStudents.as_view(), name='delete_students'),
    path('add_teachers/',views.addNewTeachers.as_view(), name='add_teachers'),
    path('list_teachers/',views.listOfTeachers.as_view(), name='list_teachers'),
    path('edit_teachers/<str:teacher_id>/',views.editTeachers.as_view(), name='edit_teachers'),
    path('delete_teachers/<str:teacher_id>/', views.deleteTeacher.as_view(), name='delete_teachers'),
    path('dashboard_teachers/', views.teacherDashboardView.as_view(), name='dashboard_teachers'),
    path('t_students/', views.AssignStudents.as_view(), name='AssignStudents'),
    path('t_attendance/', views.markAttendance.as_view(), name='t_attendance'),
    path('t_announcemments/', views.makeAnnouncemeent.as_view(), name='t_announcements'),
    path('delete_announcement/<int:ann_id>/', views.deleteAnnouncemment.as_view(), name='delete_announcement'),
    path('dashboard_students/', views.studentDashboard.as_view(), name='dashboard_students'),
    path('s_announcemments/', views.announcementView.as_view(), name='s_announcements'),
    path('s_attendance/', views.anttendanceView.as_view(), name='s_attendance'),
    # path('ajax/filter-students/', views.ajax_filter_students.as_view(), name='ajax_filter_students'),

]