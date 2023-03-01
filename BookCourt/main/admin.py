from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Users

@admin.register(Users)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('company_name', 'mobile_phone', 'email', 'url',
                    'adres', 'name_of_major', 'password')
