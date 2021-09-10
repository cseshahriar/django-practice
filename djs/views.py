import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import Post, Info

class PostView(TemplateView):
    template_name = 'djs/spinner/spinner.html'

def post_json(request):
    data = list(Post.objects.values())
    return JsonResponse(data, safe=False)
    """ 
    safe parameter is set to False , any object can be passed for serialization;
    otherwise only dict instances are allowed
    
    https://pypi.org/project/django-seed/
    for 1000 post seed to Post model
    python manage.py seed djs --number=1000
    """

""" Live search """
class InfoListView(ListView):
    model = Info
    template_name = 'djs/livesearch/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(self.model.objects.values()))
        return context