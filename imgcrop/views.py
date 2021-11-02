from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ImageCropForm, PhotoForm
from .models import Image


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


def photo_list(request):
    photos = Image.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'imgcrope/photo_list.html', {'form': form, 'photos': photos})
