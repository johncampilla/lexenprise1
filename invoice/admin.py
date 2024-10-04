from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ServicesAdmin(ImportExportModelAdmin):
    list_display = ['ar','service_rendered', 'lawyer_name', 'pf_USDamount', 'pf_PhPamount']

class Temp_BillAdmin(ImportExportModelAdmin):
    list_display = ['matter','service_rendered', 'USDamount', 'PhPamount']

admin.site.register(Bills, ServicesAdmin)
admin.site.register(TempBills, Temp_BillAdmin)

admin.site.register(TempFilingFees)
admin.site.register(TempOPE)

admin.site.register(AccountsReceivable)
admin.site.register(FilingFees)
admin.site.register(OPE)
admin.site.register(InvoiceImage)