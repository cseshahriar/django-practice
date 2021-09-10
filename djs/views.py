from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.http import JsonResponse

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