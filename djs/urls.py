from django.urls import path
from .views import PostView, post_json, InfoListView, ProductListView

urlpatterns = [
    path('post/list/', PostView.as_view(), name='post-list-view'),
    path('post/json/', post_json, name='post-json-view'),
    path('info/list/', InfoListView.as_view(), name='info-list-view'),

    path('product/list/', ProductListView.as_view(), name='product-list'),
]