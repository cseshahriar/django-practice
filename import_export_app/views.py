from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from .admin import PostResource


class MainView(TemplateView):
    template_name = 'import_export_app/main.html'

def export(request, format):
    post_resource = PostResource()
    dataset = post_resource.export()
    if format == 'csv':
        dataset_format = dataset.csv
    else:
        dataset_format = dataset.xls

    response = HttpResponse(dataset_format, content_type=f"text/{format}")
    response['Content-Disposition'] = f"attachment; filename=posts.{format}"
    return response
