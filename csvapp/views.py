import csv
from django.shortcuts import render
from users.models import CustomUser

from .models import CsvModel, Sale
from .forms import CsvModelForm

def upload_file_view(request):    
    form = CsvModelForm(request.POST or None, request.FILES or None)
    # if post request
    if form.is_valid():
        form.save()
        form = CsvModelForm() # rest
        obj = CsvModel.objects.filter(activated=False).last()
        # inser from csv
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0: # skip first lines or titles
                    pass
                else:
                    product = row[1].upper()
                    qty = row[2] if row[2] else 1 # default qty 1
                    user = CustomUser.objects.get(email=row[3])

                    Sale.objects.create(
                        product=product,
                        salesman=user,
                        quantity=int(qty)
                    )

            obj.activated = True
            obj.save()
    return render(request, 'csvapp/upload_file.html', {'form': form})