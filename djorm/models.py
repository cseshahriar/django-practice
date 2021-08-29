from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.surname}'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.surname}'


# Multiple model inheritance
class Book(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class ISBN(Book):
    book_ptr = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True
    )
    ISBN = models.CharField(max_length=100)


# Abstract Model inheritance
class BaseItem(models.Model):
    """ base class """
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['title']


class ItemA(BaseItem): # single inheritance
    content = models.TextField()

    class Meta(BaseItem.Meta):
        """ override base model meta """
        ordering = ['-created']


class ItemB(BaseItem): # single inheritance
    file = models.FileField(upload_to='djorm/abs/')


class ItemC(BaseItem): # single inheritance
    slug = models.SlugField(max_length=255, unique=True)


# proxy model inheritance
class BookContent(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class BookOrders(BookContent):
    """ 
    proxy model
    creating a proxy for the original model. 
    actualy overriting base class functionality
    """

    class Meta:
        proxy = True
        ordering = ['-created']

    def created_on(self):
        return timezone.now() - self.created