from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import upload_file_view, upload_image_file, editjs_home_view, editjs_post_detail

urlpatterns = [
    path('editjs/posts/', editjs_home_view, name='editjs_home'),
    path('editjs/posts/<int:pk>/', editjs_post_detail, name='editjs_detail'),
    path('fileUpload/', csrf_exempt(upload_file_view)),
    path('imageUpload/', csrf_exempt(upload_image_file)),
]