from django.shortcuts import render
from djorm.models import Student, Teacher
from django.db import connection
from django.db.models import Q

def student_list(request):
    """ get all """
    student_list = Student.objects.all()
    print('object list ',student_list)
    """<QuerySet [<Student: Shahriar Murol>]>"""

    print('query ', student_list.query)
    """
    query  SELECT "djorm_student"."id", "djorm_student"."first_name", "djorm_student"."surname", 
    "djorm_student"."age", "djorm_student"."classroom", "djorm_student"."teacher" FROM "djorm_student"
    """
    
    print('connection qs', connection.queries)
    """ 
    [{'sql': 'SELECT "djorm_student"."id", "djorm_student"."first_name", "djorm_student"."surname", "djorm_student"."age", 
    "djorm_student"."classroom", "djorm_student"."teacher" FROM "djorm_student" LIMIT 21', 'time': '0.000'}]
    """
    
    return render(request, 'djorm/student_list.html', {'student_list': student_list})


def filtered_student_list(request):
    """ or query """
    # sql like 
    student_list = Student.objects.filter(
        Q(surname__startswith='Murol') | Q(surname__startswith='Sarker')
    )
    print(student_list)
    return render(request, 'djorm/student_list.html', {'student_list': student_list})


def student_and_query(request):
    # sql like 
    student_list = Student.objects.filter(
        Q(surname__startswith='Murol') & Q(age__gte=27)
    )
    print(student_list)
    return render(request, 'djorm/student_list.html', {'student_list': student_list})
