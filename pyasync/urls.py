from django.urls import path
from .views import home_view, main_view, main_view_async

urlpatterns = [
    path('home_view/', home_view, name='async_home_view'),
    path('sync/', main_view, name='async_main_view'),
    path('async/', main_view_async, name='async_main_view_async')
]
