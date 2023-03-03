from django.shortcuts import render
from django.db.models import Q
from .models import Books
from .resources import BooksResource
from django.contrib import messages
from tablib import Dataset
from django.apps import apps
from django.views.generic import ListView

model = apps.get_model('main', 'Users')


def katalog(request):
    database = Books.objects.order_by('?')[:12]
    books = Books.objects.all()
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
                data[8],
                data[9]
            )
            value.save()
    return render(request, 'database/katalog.html', {'database': database, 'books': books})


def book(request, book_id):
    database = Books.objects.get(pk=book_id)
    return render(request, 'database/book.html', {'database': database})


def profile(request):
    data = model.objects.all()
    return render(request, 'database/user-profile.html', {'data': data})


class SearchResultsView(ListView):
    model = Books
    template_name = 'database/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Books.objects.filter(
            Q(Name__icontains=query)
        )
        return object_list



"""
Над этим всем страдал Олег
"""