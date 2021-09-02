from django.urls import path
from .views import qrcode_list_view

urlpatterns = [
   path('qrcode_list_view/', qrcode_list_view, name='qrcode_list_view'),
]
