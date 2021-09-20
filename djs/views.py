import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import Post, Info, Product

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



# ============== multiple objects delete =================
class ProductListView(View):
    template_name = 'djs/massoperation/product_list.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_ids = request.POST.getlist('ids[]') # from ajax
            print('product_ids--------------------------------', product_ids)
            for id in product_ids:
                product = Product.objects.get(pk=id)
                product.delete()

            return redirect('product-list')