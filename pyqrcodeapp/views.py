from django.shortcuts import render
from .models import Website


def qrcode_list_view(request):
    return render(
        request,
        'qrcode/qrcode.html',
        {
            'object_list':Website.objects.all(),
        }
    )