from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm


def index(request):
    form = UsersForm()
    return render(request, 'main/index.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('katalog')

    else:
        # GET request, present an empty form
        form = UsersForm()
    return render(request, 'main/registration.html', {"form": form})

def about(request):
    return render(request, 'main/about.html')
