# from django.views                       import View
# from django.shortcuts                   import render, redirect, get_object_or_404
# from django.contrib.auth                import authenticate, login as auth_login
# from app_Admin.forms.teacher_form       import TeacherForm
# from app_Admin.forms.student_form       import StudentForm
# from django.contrib                     import messages
# from app_Admin.models                   import Teacher,School, Student,Classroom, Attendance, Announcement, Subject
# from django.contrib.auth.decorators     import login_required
# from datetime                           import datetime
# from django.views.decorators.http       import require_POST
# from django.http                        import JsonResponse



# def ajax_filter_students(request):
#     classroom_id = request.GET.get('classroom_id')
#     if classroom_id:
#         students = Student.objects.filter(classroom_id=classroom_id)
#     else:
#         students = Student.objects.all()

#     student_data = [
#         {
#             'id': s.id,
#             'first_name': s.first_name,
#             'last_name': s.last_name,
#             'contact_no': s.contact_no,
#             'email': s.email,
#             'classroom': s.classroom.name,
#         }
#         for s in students
#     ]
#     return JsonResponse({'students': student_data})