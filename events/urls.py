from django.urls import path
from events import views

urlpatterns = [
    path("events/", views.events, name="events"),


    path("", views.event_home, name="event_home"),
    path("<int:pk>/", views.event_detail, name="event_detail"),
    path("event_create/", views.event_create, name="event_create"),
    path("<int:pk>/event_update", views.event_update, name="event_update"),
    path("<int:pk>/event_delete", views.event_delete, name="event_delete"),
]