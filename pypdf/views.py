from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic.list import ListView
from .models import Customer


class CustomerListView(ListView):
   model = Customer
   template_name = 'pdf/main.html'

def customer_render_pdf_view(request, pk, *args, **kwargs):
   template_path = 'pdf/pdf_single.html'
   context = {'object': Customer.objects.get(pk=pk)}
   # Create a Django response object, and specify content_type as pdf
   response = HttpResponse(content_type='application/pdf')
   
   # if download
   # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # if display
   response['Content-Disposition'] = 'filename="report.pdf"'

   # find the template and render it.
   template = get_template(template_path)
   html = template.render(context)

   # create a pdf
   pisa_status = pisa.CreatePDF(html, dest=response)
   # if error then show some funy view
   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response

def render_pdf_view(request):
   template_path = 'pdf/pdf.html'
   context = {'object_list': Customer.objects.all()}
   # Create a Django response object, and specify content_type as pdf
   response = HttpResponse(content_type='application/pdf')
   
   # if download
   # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # if display
   response['Content-Disposition'] = 'filename="report.pdf"'

   # find the template and render it.
   template = get_template(template_path)
   html = template.render(context)

   # create a pdf
   pisa_status = pisa.CreatePDF(html, dest=response)
   # if error then show some funy view
   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response