import random
from django.shortcuts import render
from django.utils.timezone import utc
from faker import Faker
import datetime
from concurrent.futures import ThreadPoolExecutor

from .models import *
from .thread import CreateStudentThread

fake = Faker()

def home(request):
    count = 1000
    start = datetime.datetime.now()
    CreateStudentThread(count).start() 
    return render(request, 'threading/list.html', {'message': 'success'})

def data_import(count):
    for i in range(count):
        print(i)
        Student.objects.create(
            name=fake.name(),
            email=fake.email(),
            address=fake.address(),
            age=random.randint(10, 50)
        )
        
def home2(request):
    count = 1000
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(data_import, count)
        future = executor.submit(data_import, count)
        print(future.result())
    return render(request, 'threading/list.html', {'message': 'success'})