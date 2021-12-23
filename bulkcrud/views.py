from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Product

class ProductListView(View):
    template_name = 'bulkcrud/product_list.html'
    products = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'products': self.products})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_ids = list(request.POST.getlist('ids'))

            for product_id in product_ids:
                try:
                    product = Product.objects.get(pk=product_id)
                    product.delete()
                    print('-' * 30, 'deleted')
                except Product.DoesNotExist as e:
                    print(e)

        return redirect('bulk_product_list')