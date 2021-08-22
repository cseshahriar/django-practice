from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from tfa.forms import CodeForm
from users.models import CustomUser
from .utils import send_sms

@login_required
def home_view(request):
    context = {}
    return render(request, 'tfa/home.html', context)


def auth_view(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify_view')
    return render(request, 'tfa/auth.html', {'form': form})


def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')

    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.email}: {user.code}"

        if not request.POST:
            # send sms
            send_sms(code_user, user.phone_number)

        if form.is_valid():
            input_number = form.cleaned_data.get('number')

            if str(code) == input_number:
                code.save()
                login(request, user)
                return redirect('home_view')
            else:
                return redirect('login_view')
    return render(request, 'tfa/verify.html', {'form': form})
        