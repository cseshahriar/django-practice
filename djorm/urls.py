from django.urls import path
from .views import (
    student_list,
    filtered_student_list,
    student_and_query,
    student_union_query,
    student_not_query,
    select_output_individual_fiends,
    simple_raw_query
)

urlpatterns = [
    path('student/list', student_list, name='student_list'),
    path('or/student/list', filtered_student_list, name='or_student_list'),
    path('and/student/list', student_and_query, name='and_student_list'),
    path('union/student/list', student_union_query, name='union_student_list'),
    path('not/student/list', student_not_query, name='not_student_list'),
    path('only/student/list', select_output_individual_fiends, name='only_student_list'),
    path('simple/raw/student/list', simple_raw_query, name='simple_raw_student_list'),
]
