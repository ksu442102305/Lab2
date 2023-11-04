from django.shortcuts import render, redirect
from .models import Student, Course


def students(request):
    students_list = Student.objects.all()
    return render(request, 'students.html', {'students_list': students_list})


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student = Student.objects.create(name=name)
        student.save()
        return redirect('students')
    return render(request, 'add_student.html')


def courses(request):
    courses_list = Course.objects.all()
    return render(request, 'courses.html', {'courses_list': courses_list})


def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course = Course.objects.create(name=name)
        course.save()
        return redirect('courses')
    return render(request, 'add_course.html')


def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    available_courses = Course.objects.exclude(students=student)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = Course.objects.get(pk=course_id)
        student.courses.add(course)
        return redirect('details', student_id=student_id)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})
