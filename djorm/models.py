from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import CustomUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from polymorphic.models import PolymorphicModel
from django.utils.translation import gettext as _

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
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class ISBN(Book, Article):
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

# sql optimizations
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager() # custom manager
    
    class Meta:
        verbose_name_plural = 'products'
        ordering = ['-created']

    def __str__(self):
        return self.title

class ProductBook(Product):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class Cupboard(Product):
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)


# GenericForeignKey
class ProductClass(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('bookmodel', 'cupboardmodel')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class ProductBase(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager() # custom manager
    
    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return self.title


class BookModel(ProductBase):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    m2m = models.ManyToManyField(
        ProductClass,
        related_name="bookmodel",
        related_query_name='bookmodel'
    )

class CupboardModel(ProductBase):
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)
    m2m = models.ManyToManyField(
        ProductClass,
        related_name="cupboardmodel",
        related_query_name='cupboardmodel'
    )

# django polymorphic
class Project(PolymorphicModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ArtProject(Project):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class ResearchProject(Project):
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)

# for transactions atomics
class Customer(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.balance}' 


class Bank(models.Model):
    payor = models.CharField(max_length=255)
    payee = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.amount)


# models for aggregation
class AggregationBook(models.Model):
  title = models.CharField(_("title"), max_length=255)
  authors = models.CharField(_("authors"), max_length=255)
  average_rating = models.FloatField(_("average rating"))
  isbn = models.CharField(_("isbn"), max_length=150)
  isbn13 = models.CharField(_("isbn 13"), max_length=150)
  language_code = models.CharField(_("language code"), max_length=10)
  num_pages = models.IntegerField(_("number of pages"))
  ratings_count = models.BigIntegerField(_("rating count"))
  text_review_count = models.BigIntegerField(_("text review count"))
  publication_date = models.DateField(_("publication date"))
  publisher = models.CharField(_("publisher"), max_length=150) 

  def __str__(self):
      return self.title


class Details(models.Model):
    name = models.CharField(_("name"), max_length=255)
    age = models.CharField(_("age"), max_length=255)