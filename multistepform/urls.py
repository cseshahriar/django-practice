from django.urls import path

from .views import multi_step_form, multistep_list

urlpatterns = [
    path('multistep_list/', multistep_list, name='multistep_list'),
    path('stepform/', multi_step_form, name='stepform'),
]
