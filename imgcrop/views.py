from django.shortcuts import render
from .forms import ImageCropForm
from .models import Image
from django.http import JsonResponse


def crop_view(request):
    """ image cropper view """
    obj = Image.objects.last()
    form = ImageCropForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return JsonResponse(
            {'message': 'works'}
        )

    context = {
        'form': form,
        'obj': obj
    }
    return render(request, 'imgcrope/img_crop.html', context)