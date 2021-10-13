from django.shortcuts import render
from events.models import Event
from django.http import HttpResponse

def event_home(request):
    data = {
        "events": Event.objects.all()
    }
    return render(request, 'events/home.html', data)

def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist as e:
        return HttpResponse(e)

    data = {
        "event": event
    }
    return render(request, 'events/detail.html', data)