from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Document

class UploadView(TemplateView):
    template_name = 'djdropzone/upload.html'

def file_upload_view(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Document.objects.create(upload=my_file)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})
