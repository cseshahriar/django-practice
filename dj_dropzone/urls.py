from django.urls import path
from .views import UploadView, file_upload_view

urlpatterns = [
    path('dropzone/', UploadView.as_view(), name='upload_with_dropzone'),
    path('file_upload_view', file_upload_view, name='file_upload_view'),
]