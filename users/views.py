from django.shortcuts import render, reverse
from django.contrib.auth import logout, authenticate, login
from .forms import UserCreateForm
from django.http import HttpResponseRedirect


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def cadastrar(request):
    if request.method != 'POST':
        form = UserCreateForm()
    else:
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'users/cadastrar.html', context)
