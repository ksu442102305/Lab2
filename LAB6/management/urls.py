from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('add_student/', views.add_student, name='add_student'),  # Add this line
    path('courses/', views.courses, name='courses'),
    path('add_course/', views.add_course, name='add_course'),
    path('details/<int:student_id>/', views.details, name='details'),
]
