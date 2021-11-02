from django.urls import path
from .views import crop_view, photo_list
urlpatterns = [
    path('cropper/', crop_view, name='crop_view'),
    path('cropper2/', photo_list, name='photo_list'),
]