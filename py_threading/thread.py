import threading
import random

from faker import Faker
fake = Faker()

from .models import *


class CreateStudentThread(threading.Thread):
    
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)
        
    def run(self):
        try:
            count = 100
            for i in range(self.total):
                print(i)
                Student.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    address=fake.address(),
                    age=random.randint(10, 50)
                )
        
        except Exception as e:
            print(e)