from django.urls import path
from .views import home, home2

urlpatterns = [
    path('', home, name='home'),
    path('v2/', home2, name='home'),
]