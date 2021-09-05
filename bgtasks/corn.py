from .models import Test, Document
from datetime import datetime
from django.http import HttpResponse

def my_bgtask():
    print('my_bgtask---------------------------------------------------------')
    Test.objects.create(name='test')
    

def document_expire_check():
    print('document_expire_check---------------------------------------------')
    today = datetime.today().strftime('%Y-%m-%d')
    print(today)
    qs = Document.objects.all()
    for doc in qs:
        exp = doc.expire_date.strftime('%Y-%m-%d')
        if exp < today:
            doc.expire = True
            doc.save()