from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Books


@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Author', 'Description', 'Price', 'Remainder', 'Image', 'NumberOfPages',
                    'SourceName', 'Genre')
