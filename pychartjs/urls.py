from django.urls import path
from .views import ClubCharView

urlpatterns = [
 path('clubs/char', ClubCharView.as_view(), name='club_chart'),
]