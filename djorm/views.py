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
    # sql or query
    student_list = Student.objects.filter(
        Q(surname__startswith='Murol') | Q(surname__startswith='Sarker')
    )
    print(student_list)
    return render(request, 'djorm/student_list.html', {'student_list': student_list})


def student_and_query(request):
    # sql and query
    student_list = Student.objects.filter(
        Q(surname__startswith='Murol') & Q(age__gte=27)
    )
    print(student_list)
    return render(request, 'djorm/student_list.html', {'student_list': student_list})


def student_union_query(request):
     # student with teacher union query
    student_list = Student.objects.all().values_list('first_name').union(Teacher.objects.all().values_list('first_name'))
    print(student_list)
    print(student_list.query)
    print(connection.queries)
    """ 
    SELECT "djorm_student"."first_name" FROM "djorm_student" UNION SELECT "djorm_teacher"."first_name" FROM "djorm_teacher"

    [{'sql': 'SELECT "djorm_student"."first_name" FROM "djorm_student" 
    NION SELECT "djorm_teacher"."first_name" FROM "djorm_teacher" LIMIT 21', 'time': '0.001'}]
    """
    return render(request, 'djorm/union_student_list.html', {'student_list': student_list})


def student_not_query(request):
    student_list = Student.objects.exclude(
        Q(age=26) |
        Q(surname__startswith='Murol')
    ) # where not age = 21
    print(student_list.query)
    print(connection.queries)
    # filter(age_get=18)
    # filter(age_lte=60)
    """
    SELECT "djorm_student"."id", "djorm_student"."first_name", "djorm_student"."surname",
    "djorm_student"."age", "djorm_student"."classroom", "djorm_student"."teacher" FROM 
    "djorm_student" WHERE NOT (("djorm_student"."age" = 26 OR "djorm_student"."surname" LIKE Murol% ESCAPE '
    """
    return render(request, 'djorm/union_student_list.html', {'student_list': student_list})

def select_output_individual_fiends(request):
    object_list = Student.objects.filter(classroom=1).only('first_name', 'age')
    print(object_list.query)
    print(connection.queries)
    """
    SELECT "djorm_student"."id", "djorm_student"."first_name", "djorm_student"."age"
    FROM "djorm_student" WHERE "djorm_student"."classroom" = 1
    """

    return render(request, 'djorm/select_individual_fiend.html', {'object_list': object_list})



def simple_raw_query(request):
    # object_list = Student.objects.raw("SELECT * FROM djorm_student")
    object_list = Student.objects.raw("SELECT * FROM djorm_student WHERE age=27")
    
    # object_list = Student.objects.raw(""" 
    # SELECT "djorm_student"."id", "djorm_student"."first_name", 
    # "djorm_student"."age" FROM "djorm_student" 
    # """)

    print(object_list.query)
    print(connection.queries)
    return render(request, 'djorm/simple_raw_qs.html', {'object_list': object_list})
