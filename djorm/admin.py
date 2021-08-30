from django.contrib import admin
from .models import (
    Teacher, Student, Category, Product, ProductBook, Cupboard,
    ProductClass, BookModel, CupboardModel,
    Project, ArtProject, ResearchProject
)
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter
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



@admin.register(ArtProject)
class ArtProjectAdmin(PolymorphicChildModelAdmin):
    pass

@admin.register(ResearchProject)
class ResearchProjectAdmin(PolymorphicChildModelAdmin):
    pass

@admin.register(Project)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Project  # Optional, explicitly set here.
    child_models = (ArtProject, ResearchProject)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.