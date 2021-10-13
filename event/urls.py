from django.urls import path
from .views import EventCalendarView, load_events

urlpatterns = [
    path('event/', EventCalendarView.as_view(), name='event_list'),
    path('event/ajax/', load_events, name='event_ajax')
]