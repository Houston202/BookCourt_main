from django.shortcuts import render
from .models import Books
from .resources import BooksResource
from django.contrib import messages
from tablib import Dataset
from django.apps import apps
from django.http import HttpResponse

model = apps.get_model('main', 'Users')


def home_page(request):
    database = Books.objects.all()
    return render(request, 'database/database_home.html', {'database': database})


def katalog(request):
    database = Books.objects.all()
    if request.method == 'POST':
        books_resource = BooksResource()
        dataset = Dataset()
        new_books = request.FILES['file']

        if not new_books.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'database/katalog.html')

        imported_data = dataset.load(new_books.read(), format='xlsx')
        for data in imported_data:
            value = Books(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8]
            )
            value.save()
    return render(request, 'database/katalog.html', {'database': database})


def profile(request):
    data = model.objects.all()
    return render(request, 'database/user-profile.html', {'data': data})


def import_data_to_db(request):
    if request.method == 'POST':
        books_resource = BooksResource()
        dataset = Dataset()
        new_books = request.FILES['file']

        if not new_books.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'database/create.html')

        imported_data = dataset.load(new_books.read(), format='xlsx')
        for data in imported_data:
            value = Books(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8]
                )
            value.save()
    return render(request, 'database/create.html')



"""
Над этим всем страдал Олег
"""