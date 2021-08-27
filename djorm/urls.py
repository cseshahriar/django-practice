from django.urls import path
from .views import student_list, filtered_student_list, student_and_query

urlpatterns = [
    path('student/list', student_list, name='student_list'),
    path('or/student/list', filtered_student_list, name='or_student_list'),
    path('and/student/list', student_and_query, name='and_student_list'),
]
