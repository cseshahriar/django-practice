
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse

from .models import Event


class EventCalendarView(TemplateView):
    template_name = 'event/event.html'

    def get_context_data(self, **kwargs):
        context = super(EventCalendarView, self).get_context_data(**kwargs)
        return context

# This is my custom JSON Response

def load_events(request):
    """ load events """    
    data = list(Event.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
