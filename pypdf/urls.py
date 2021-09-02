from django.urls import path
from .views import render_pdf_view, customer_render_pdf_view, CustomerListView

urlpatterns = [
    path('pdf/customer/', CustomerListView.as_view(), name='customer_list'),
    path('pdf/customer/', render_pdf_view, name='customer_pdf'),
    path(
        'pdf/<int:pk>/download/',
        customer_render_pdf_view,
        name='customer_render_pdf_view'
    ),
]