from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class Docs_Admin(ImportExportModelAdmin):
    list_display = ['DocDate','task_detail','Description', 'DocsPDF']
    

admin.site.register(task_detail)
admin.site.register(FilingDocs, Docs_Admin)