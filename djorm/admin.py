from django.contrib import admin
from .models import Teacher, Student, Category, Product, ProductBook, Cupboard

admin.site.register(Teacher)
admin.site.register(Student)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductBook)
admin.site.register(Cupboard)