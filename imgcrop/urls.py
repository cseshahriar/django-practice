from django.urls import path
from .views import crop_view
urlpatterns = [
    path('cropper/', crop_view, name='crop_view'),
]