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


""" 3 django inheritance options """

# Abstract Model
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
