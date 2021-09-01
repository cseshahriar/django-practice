from django.urls import path
from .views import render_pdf_view

urlpatterns = [
    path('pdf/customer/', render_pdf_view, name='customer_pdf'),
]