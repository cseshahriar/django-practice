import random
from django.shortcuts import render
from django.utils.timezone import utc
from faker import Faker
from .models import *
from .thread import CreateStudentThread
import datetime

fake = Faker()

def home(request):
    count = 1000
    start = datetime.datetime.now()
    CreateStudentThread(count).start() 
    return render(request, 'threading/list.html', {'message': 'success'})