from django.urls import  path
from .views import ProductListView
urlpatterns = [
    path('bulkcrud/list/', ProductListView.as_view(), name='bulk_product_list'),
]