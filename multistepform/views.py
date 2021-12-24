from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MultiStepFormModel
from .forms import MultiStepFormModelForm

def multistep_list(request):
    object_list = MultiStepFormModel.objects.all()
    return render(request, 'multistep/list.html', {'object_list': object_list})
    
def multi_step_form(request):
    if request.method == 'POST':
        print('post----------------------------------------------------------')
        form = MultiStepFormModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("Successfully-----------------------------------------")
            messages.success(request, 'Data saved successfully')
            return redirect('multistep_list')
        else:
            messages.error(request, 'Oops! something went wrong')
            return redirect('stepform')
    else:
        form = MultiStepFormModelForm()
        return render(request, 'multistep/step_form.html', {'form': form})