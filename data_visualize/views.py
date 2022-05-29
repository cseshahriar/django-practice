from django.shortcuts import render
from .models import Sale
from .utils import get_plot


def main_view(request):
    qs = Sale.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x, y)
    return render(request, 'data/index.html', {'chart': chart})