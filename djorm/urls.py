from django.urls import path
from .views import student_list, filtered_student_list

urlpatterns = [
    path('student/list', student_list, name='student_list'),
    path('filtered/student/list', filtered_student_list, name='filtered_student_list'),
]
