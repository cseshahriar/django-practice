from django.urls import path
from .views import main_view

urlpatterns = [
    path('chart/', main_view, name='chart_view'),
]