from django.urls import path
from .views import PostView, post_json, InfoListView

urlpatterns = [
    path('post/list/', PostView.as_view(), name='post-list-view'),
    path('post/json/', post_json, name='post-json-view'),
    path('info/list/', InfoListView.as_view(), name='info-list-view'),
]