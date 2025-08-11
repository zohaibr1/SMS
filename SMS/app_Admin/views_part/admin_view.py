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
from django.http                        import JsonResponse


#adding new student
class addNewStudents(View):
    def get(self,request):
        form = StudentForm()             
        return render(request,'add_students.html',{'form': form})
    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
                form.save()
                if request.headers.get('X-Requested-With')=='XMLHttpRequest':
                    return JsonResponse({'message':'Student added succefully'},status=200)
                messages.success(request, 'Student added successfully!')
                return redirect('list_students')
        else:   
            if request.headers.get('X-Requested-With')=='XMLHttprequest':
                return JsonResponse({'error':form.errors},status=400)              
            
            return render(request,'add_students.html',{'form':form}) 
#list of students
class listOfStudents(View):
    def get(self,request):
        list_students=Student.objects.all()  
        if request.headers.get('X-Requested-With')=='XMLHttpRequest':
            student_data=[]
            for student in list_students:
                student_data.append({
                    "id": student.id,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "email": student.email,
                    "classroom":student.classroom.name if student.classroom else '',
                    "contact_no": student.contact_no,
                    "subjects": [subject.name for subject in student.subject.all()],
                    "address":student.address,
                })
                
            return JsonResponse({'students':student_data},status=200)
        return render(request,'list_students.html',{'list_students':list_students})
    
#Edit Students
class editStudents(View):
    def get(self, request,student_id):
        student=get_object_or_404(Student,pk=student_id)
        return render(request, 'edit_students.html', {
        'student': student,
        'form': StudentForm(instance=student)
    })
    def post(self,request,student_id):
            student=get_object_or_404(Student,pk=student_id)

            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.email = request.POST.get('email')
            student.contact_no = request.POST.get('contact_no')
            student.address = request.POST.get('address')
            classroom_id=request.POST.get('classroom')
            if classroom_id:
                try:
                    student.classroom = Classroom.objects.get(id=classroom_id)
                except Classroom.DoesNotExist:
                    return JsonResponse({'error':'invalid class_ID'},status=400)
            student.save()
            # Handle many-to-many
            student.subject.set(request.POST.getlist('subject'))
            if request.headers.get('X-Requested-With')== 'XMLHttpRequest':
                return JsonResponse({'message':'Student Updated successfully!!'},status=200)
        

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
            if request.headers.get('X-Requested-With')=='XMLHttpRequest':
                return JsonResponse({'message':'Teacher added succefully'},status=200)
            messages.success(request, 'Teacher added successfully!')
            return redirect('list_teachers')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
            print(form.errors)
            return render(request, 'add_teachers.html', {'form': form,})
        
# list of teachers
class listOfTeachers(View):
    def get(self, request):
        list_teachers = Teacher.objects.all()

       
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            teachers_data = []
            for teacher in list_teachers:
                teachers_data.append({
                    "id": teacher.id,
                    "first_name": teacher.first_name,
                    "last_name": teacher.last_name,
                    "email": teacher.email,
                    "contact_no": teacher.contact_no,
                    "subjects": [subject.name for subject in teacher.subject.all()],
                    "classrooms": [cls.name for cls in teacher.classroom.all()],
                    "Join_date":teacher.Join_date,
                    "address":teacher.address,
                })
            return JsonResponse({"teachers": teachers_data}, status=200)
        
        return render(request, 'list_teachers.html', {'list_teachers': list_teachers})

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
            error='join Date is required.'
            return self.handle_error(request,teacher,error)
        try:
            teacher.Join_date = datetime.strptime(join_date_str, '%Y-%m-%d').date( )
        except ValueError:
            error='put date in given order YYYY-MM-DD'
            return self.handle_error(request,teacher,error)
        teacher.save()

        # Handle many-to-many
        teacher.subject.set(request.POST.getlist('subject'))
        teacher.classroom.set(request.POST.getlist('classroom'))
        if request.headers.get('X-Requested-with')=='XMLHttpRequest':
            return JsonResponse({'message':'teacher updated succefully'},status=200)
        return redirect('list_teachers')
    #use to avoid redundancy
    def handle_error(self, request, teacher, error_message):
        """Helper to handle errors for both AJAX and normal POST."""
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'error': error_message}, status=400)

        return render(request, 'edit_teachers.html', {
            'teacher': teacher,
            'form': TeacherForm(instance=teacher),
            'error': error_message
        })    
#DELETE teachers
class deleteTeacher(View):
    def get(self,request,teacher_id):
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        return render(request,'delete_teachers.html',{'teacher':teacher})
    def post(self,request,teacher_id):
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        teacher.delete()
        return redirect('list_teachers')
    
