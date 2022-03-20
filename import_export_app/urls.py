from django.urls import path
from .views import export, MainView


urlpatterns = [
    path('export/posts/', MainView.as_view(), name='export_post_main'),
    path('<str:format>/export/posts/', export, name='export_post'),
]