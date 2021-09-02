from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Club

class ClubCharView(TemplateView):

    template_name = "pychartjs/chart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Club.objects.all()
        return context