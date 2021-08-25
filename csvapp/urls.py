from django.urls import path
from .views import upload_file_view

urlpatterns = [
    path('csv_upload/', upload_file_view, name='csv_upload'),
]