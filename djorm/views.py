from django.db import DatabaseError, connection, transaction
from django.db.models import F, Q, Sum, Max, Min, Avg, FloatField
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .forms import PaymentForm
from .models import (AggregationBook, Bank, BookModel, Category, Cupboard,
                     CupboardModel, Customer, Product, ProductBook,
                     ProductClass, Student, Teacher)

""" orm properties:
    exact, iexact
    contains, icontains
    in, gt, gte, lt, lte
    startswith
    isstartswith
    endswith
    iendswith
    range
    year
    month
    day
    week_day
    isnull
    search
    regex
    iregex
"""

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
    sql = "SELECT * FROM djorm_student WHERE age=27"
    object_list = Student.objects.raw(sql)[:1]
    
    # object_list = Student.objects.raw(""" 
    # SELECT "djorm_student"."id", "djorm_student"."first_name", 
    # "djorm_student"."age" FROM "djorm_student" 
    # """)

    return render(request, 'djorm/simple_raw_qs.html', {'object_list': object_list})


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def custom_sql_qs(request):
    """ 
    custom sql query fetchone, fetchall, dictfetchall()
    """
    with connection.cursor() as cursor:
        cursor = connection.cursor()
        # cursor.execute("SELECT count(*) from djorm_student")
        cursor.execute("SELECT * from djorm_student")
        # studen_count = cursor.fetchone()
        # {'studen_count': studen_count}
        # object_list = cursor.fetchall()
        object_list = dictfetchall(cursor)
        print(object_list) 
    return render(request, 'djorm/custom_raw_qs.html', {'object_list': object_list})


# inheritance optimizations
def product_all(request):
    # products = Product.objects.all() # 11 qs
    products = Product.objects.all().select_related('productbook', 'cupboard') # 1 qs
    """
    SELECT "djorm_product"."id",
       "djorm_product"."title",
       "djorm_product"."description",
       "djorm_product"."image",
       "djorm_product"."slug",
       "djorm_product"."price",
       "djorm_product"."in_stock",
       "djorm_product"."is_active",
       "djorm_product"."created",
       "djorm_product"."updated",
       "djorm_productbook"."product_ptr_id",
       "djorm_productbook"."publisher",
       "djorm_productbook"."author",
       "djorm_cupboard"."product_ptr_id",
       "djorm_cupboard"."shelves",
       "djorm_cupboard"."author"
        FROM "djorm_product"
        LEFT OUTER JOIN "djorm_productbook"
            ON ("djorm_product"."id" = "djorm_productbook"."product_ptr_id")
        LEFT OUTER JOIN "djorm_cupboard"
            ON ("djorm_product"."id" = "djorm_cupboard"."product_ptr_id")
        WHERE "djorm_product"."is_active"
        ORDER BY "djorm_product"."created" DESC
    """
    return render(request, 'djorm/product_all.html', {'products': products})


def generic_product_all(request):
    # products = ProductClass.objects.all() # 5qs
    products = ProductClass.objects.all().select_related('content_type') # 5qs
    # cupboards = CupboardModel.objects.all()
    # books = BookModel.objects.all()
    # products = cupboards.union(books)

    return render(request, 'djorm/generic_product_all.html', {'products': products})


# open a transaction
# @transaction.atomic
def process_payment(request):

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            input_payor = form.cleaned_data['payor']
            input_payee = form.cleaned_data['payee']
            input_amount = form.cleaned_data['amount']
        
        with transaction.atomic(): # if any db execution fail rollback else save
            # All operations should be executed

            # sender, transaction problem can be here
            payor = Customer.objects.select_for_update.get(name=input_payor)
            payor.balance -= input_amount
            payor.save()

            # receiver, transact problem can be hrere
            payee = Customer.objects.select_for_update.get(name=input_payee)
            payee.balance += input_amount
            payee.save()

            # Customer.objects.filter(named=input_payor).update(balance=F('balance') - z)
            # Customer.objects.filter(named=input_payee).update(balance=F('balance') + z)

            return HttpResponseRedirect('/')
    else:
        form = PaymentForm()

    return render(request, 'djorm/payment_form.html', {'form': form})



def dj_aggregations(request):
    book_count = AggregationBook.objects.count()
    ratings_count = AggregationBook.objects.all().aggregate(Sum('ratings_count'))
    max_rating = AggregationBook.objects.all().aggregate(Max('average_rating'))
    min_rating = AggregationBook.objects.all().aggregate(Min('average_rating'))

    avg = AggregationBook.objects.all().aggregate(Avg('average_rating'))
    rating_diff = AggregationBook.objects.aggregate(
        rating_diff=Max('average_rating', output_field=FloatField()) - Avg('average_rating')
    )
    authors_rating = AggregationBook.objects.filter(
        authors="Shahriar").aggregate(
            Avg('average_rating'), Min('average_rating'), Max('average_rating')
        )

    data = {
        'count': book_count,
        'ratings_count': ratings_count,
        'max_rating': max_rating,
        'min_rating': min_rating,
        'avg': avg,
        'rating_diff': rating_diff,
        'authors_rating': authors_rating
    }
    return JsonResponse(data)


