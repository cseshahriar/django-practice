from django.shortcuts import render
from django.http import HttpResponse

from .models import CsvModel, Sale
from .forms import CsvModelForm

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    # if post request
    if form.is_valid():
        form.save()
        form = CsvModelForm() # rest
    return render(request, 'csvapp/upload_file.html', {'form': form})