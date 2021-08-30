from django.contrib import admin
from .models import (
    Teacher, Student, Category, Product, ProductBook, Cupboard,
    ProductClass, BookModel, CupboardModel
)

admin.site.register(Teacher)
admin.site.register(Student)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductBook)
admin.site.register(Cupboard)

admin.site.register(ProductClass)
admin.site.register(BookModel)
admin.site.register(CupboardModel)