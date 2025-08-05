from django.views                       import View
from django.shortcuts                   import render, redirect, get_object_or_404
from django.contrib.auth                import authenticate, login as auth_login
from app_Admin.forms.teacher_form       import TeacherForm
from app_Admin.forms.student_form       import StudentForm
from django.contrib                     import messages
from app_Admin.models                   import Teacher,School, Student,Classroom, Attendance, Announcement, Subject
from django.contrib.auth.decorators     import login_required
from datetime                           import datetime
from django.views.decorators.http       import require_POST



#adding new student
class addNewStudents(View):
    def get(self,request):
        form = StudentForm()             
        return render(request,'add_students.html',{'form': form})
    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, 'Student added successfully!')
                return redirect('list_students')
        print(form.errors)
        return render(request,'add_students.html',{'form':form}) 
#list of students
class listOfStudents(View):
    def get(self,request):
        list_students=Student.objects.all()       
        return render(request,'list_students.html',{'list_students':list_students})
    
#Edit Students
class editStudents(View):
    def get(self,
            request,student_id):
        student=get_object_or_404(Student,pk=student_id)
        return render(request, 'edit_students.html', {
        'student': student,
        'form': StudentForm(instance=student)
    })
    def post(Self,request,student_id):
        student=get_object_or_404(Student,pk=student_id)
        if request.method=='POST':
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.email = request.POST.get('email')
            student.contact_no = request.POST.get('contact_no')
            student.address = request.POST.get('address')
            classroom_id=request.POST.get('classroom')
            if classroom_id:
                student.classroom = Classroom.objects.get(id=classroom_id)
            student.save()

        # Handle many-to-many
        student.subject.set(request.POST.getlist('subject'))


        return redirect('list_students')

#delete Students

class deleteStudents(View):
    def get(self,request,student_id):
        student=get_object_or_404(Student,pk=student_id)
        return render(request,'delete_students.html', {'student':student})
    def post(self,request,student_id):
        student=get_object_or_404(Student,pk=student_id)
        student.delete()
        return redirect('list_students')

#add new teacher
class addNewTeachers(View):
    def get(self,request):
        form = TeacherForm()             
        return render(request,'add_teachers.html',{'form': form})
    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.school = School.objects.first() 
            teacher.save()
            form.save_m2m()  # save many-to-many fields like subjects/classrooms
            messages.success(request, 'Teacher added successfully!')
            return redirect('list_teachers')
        else:
            print(form.errors)
            return render(request, 'add_teachers.html', {'form': form,})
        
# list of teachers
class listOfTeachers(View,):
    def get(self,request):
        list_teachers=Teacher.objects.all()
        return render(request,'list_teachers.html',{'list_teachers':list_teachers})

#Edit teachers
class editTeachers(View):
    def get(self,request,teacher_id):
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        return render(request, 'edit_teachers.html', {
            'teacher': teacher,
            'form': TeacherForm(instance=teacher)
        })
        
    def post(self,request,teacher_id):
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.email = request.POST.get('email')
        teacher.contact_no = request.POST.get('contact_no')
        teacher.address = request.POST.get('address')

        join_date_str = request.POST.get('Join_date')
        if not join_date_str:
            return render(request, 'edit_teachers.html', {
                'teacher': teacher,
                'form': TeacherForm(instance=teacher),
                'error': 'Join Date is required.',
            })
        try:
            teacher.Join_date = datetime.strptime(join_date_str, '%Y-%m-%d').date( )
        except ValueError:
            return render(request, 'edit_teachers.html', {
                'teacher': teacher,
                'form': TeacherForm(instance=teacher),
                'error': 'Invalid date format. Please use YYYY-MM-DD.',
            })

        teacher.save()

        # Handle many-to-many
        teacher.subject.set(request.POST.getlist('subject'))
        teacher.classroom.set(request.POST.getlist('classroom'))

        return redirect('list_teachers')

#DELETE teachers
class deleteTeacher(View):
    def get(self,request,teacher_id):
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        return render(request,'delete_teachers.html',{'teacher':teacher})
    def post(self,request,teacher_id):
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        teacher.delete()
        return redirect('list_teachers')
    
