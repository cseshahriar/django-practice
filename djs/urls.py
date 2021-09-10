from django.urls import path
from .views import PostView, post_json

urlpatterns = [
    path('post/list/', PostView.as_view(), name='post-list-view'),
    path('post/json/', post_json, name='post-json-view'),
]