from django.urls import path
from estates.views import (
    estate_property_defer, estate_property_only, estate_property_exclude
)

urlpatterns = [
    path("defer", estate_property_defer, name="properties_defer"),
    path("only", estate_property_only, name="properties_only"),
    path("exclude", estate_property_exclude, name="properties_exclude"),
]
