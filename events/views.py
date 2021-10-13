from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
from events.forms import EventForm


def events(request):
    data = {
        "object_list": Event.objects.filter(is_active=True)
    }
    return render(request, 'events/events.html', data)


# ================================= crud ======================================
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


def event_create(request):
    return process_event_form(request)


def event_update(request, pk):
    try:
        return process_event_form(request, pk)
    except:
        return HttpResponse("Event doesn't exists")

def process_event_form(request, pk=None):
    event = Event.objects.get(pk=pk) if pk is not None else None
    print('-' * 50, event)

    form = EventForm(request.POST or None, instance=event)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
            return HttpResponse("New event created!!" if event is None else "Updated event!")
        except Exception as e:
            return HttpResponse("Error with event processing.", e)

    context = {
        "form": form,
        "event": event
    }

    return render(request, 'events/form.html', context)


def event_delete(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        if event:
            event.delete()
            return HttpResponse("Event deleted!")
    except:
        return HttpResponse("Event doesn't exist")