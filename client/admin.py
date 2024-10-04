from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class Client_Data_Admin(ImportExportModelAdmin):
    list_display = ['client_number','client_name', 'entity_type', 'email', 'industry']

class NatureOfBusiness_Admin(ImportExportModelAdmin):
    list_display = ['industry']

class Contact_Person_Admin(ImportExportModelAdmin):
    list_display = ['client', 'contact_person']

# Register your models here.
admin.site.register(Country)
admin.site.register(Client_Bill_Details)
admin.site.register(Client_Data, Client_Data_Admin)
admin.site.register(NatureOfBusiness, NatureOfBusiness_Admin)
admin.site.register(Contact_Person, Contact_Person_Admin)
