from django.urls import path
from events import views

urlpatterns = [
    path("", views.event_home, name="event_home"),
    path("<int:pk>/", views.event_detail, name="event_detail"),
]