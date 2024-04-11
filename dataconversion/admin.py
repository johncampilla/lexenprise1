from django.contrib import admin
from .models import Csv, csv_client, egazette, csv_matter, csv_task, csv_duedates, csv_AR
from import_export.admin import ImportExportModelAdmin 


class csv_client_Admin(ImportExportModelAdmin):
    list_display = ['CLIENTNUMBER','ClientName','EMail','CountryCode','Industry','ContactPerson']

class csv_matter_Admin(ImportExportModelAdmin):
    list_display = ['Client_Number','ApplicationNo', 'Case1', 'Case2','Applicant']

class csv_duedates_Admin(ImportExportModelAdmin):
    list_display = ['ClientNo','ApplicationNo', 'DueDates', 'DueCode','Activities']

class csb_AR_Admin(ImportExportModelAdmin):
    list_display = ['Client_Number', 'ApplicationNo', 'BillNumber', 'BillAmount', 'PesoAmount']

class csv_Admin(ImportExportModelAdmin):
    list_display = ['file_name']

class csv_egazette_Admin(ImportExportModelAdmin):
    list_display = ['Application_Number', 'Filing_Date', 'Mark', 'Applicant', 'Nice_class']

class csv_task_Admin(ImportExportModelAdmin):
    list_display = ['ClientNo', 'ApplicationNo', 'CaseOfficer', 'ActivityDate', 'TaskDescription']


# Register your models here.
admin.site.register(Csv, csv_Admin)
admin.site.register(csv_client, csv_client_Admin)
admin.site.register(csv_matter, csv_matter_Admin)
admin.site.register(csv_task, csv_task_Admin)
admin.site.register(egazette, csv_egazette_Admin)
admin.site.register(csv_duedates, csv_duedates_Admin)
admin.site.register(csv_AR, csb_AR_Admin)

