from django.contrib import admin
from .models import Csv, csv_client, egazette, csv_matter, csv_task, csv_duedates, csv_AR, csv_casefolder, csv_apptype, csv_appstat, csv_officers, csv_docs, csv_applicant, csv_templates, csv_industry, csv_stages, csv_clientfile
from import_export.admin import ImportExportModelAdmin 


# class csv_client_Admin(ImportExportModelAdmin):
#     list_display = ['CLIENTNUMBER','ClientName','EMail','CountryCode','Industry','ContactPerson']

# class csv_casefolder_Admin(ImportExportModelAdmin):
#     list_display = ['clientnumber','folder_description']

# class csv_matter_Admin(ImportExportModelAdmin):
#     list_display = ['Client_Number','ApplicationNo', 'Case1', 'Case2','Applicant']

# class csv_duedates_Admin(ImportExportModelAdmin):
#     list_display = ['ClientNo','ApplicationNo', 'DueDates', 'DueCode','Activities']

# class csb_AR_Admin(ImportExportModelAdmin):
#     list_display = ['Client_Number', 'ApplicationNo', 'BillNumber', 'BillAmount', 'PesoAmount']

# class csv_Admin(ImportExportModelAdmin):
#     list_display = ['file_name']

# class csv_egazette_Admin(ImportExportModelAdmin):
#     list_display = ['Application_Number', 'Filing_Date', 'Mark', 'Applicant', 'Nice_class']

# class csv_task_Admin(ImportExportModelAdmin):
#     list_display = ['ClientNo', 'ApplicationNo', 'CaseOfficer', 'ActivityDate', 'TaskDescription']

# # Reference Lookup Tables
# class csv_apptype_Admin(ImportExportModelAdmin):
#     list_display = ['ApplicationType', 'Description']

# class csv_appstat_Admin(ImportExportModelAdmin):
#     list_display = ['AppStat', 'ApplicationStatus']

# class csv_officers_Admin(ImportExportModelAdmin):
#     list_display = ['CaseOfficers', 'OfficerName']

# class csv_docs_Admin(ImportExportModelAdmin):
#     list_display = ['DocumentType', 'Description']

# class csv_applicant_Admin(ImportExportModelAdmin):
#     list_display = ['ApplicantCode', 'ApplicantName']

# class csv_templates_Admin(ImportExportModelAdmin):
#     list_display = ['DocumentCode', 'Description', 'ApplicationType', 'DocPath']

# class csv_industry_Admin(ImportExportModelAdmin):
#     list_display = ['Industry', 'Description']

# class csv_stages_Admin(ImportExportModelAdmin):
#     list_display = ['Stage', 'Description']

# class csv_clientfile_Admin(ImportExportModelAdmin):
#     list_display = ['client_number', 'client_name']

# # Register your models here.
# admin.site.register(Csv, csv_Admin)
# admin.site.register(csv_casefolder, csv_casefolder_Admin)
# admin.site.register(csv_client, csv_client_Admin)
# admin.site.register(csv_matter, csv_matter_Admin)
# admin.site.register(csv_task, csv_task_Admin)
# admin.site.register(egazette, csv_egazette_Admin)
# admin.site.register(csv_duedates, csv_duedates_Admin)
# admin.site.register(csv_AR, csb_AR_Admin)
# admin.site.register(csv_apptype, csv_apptype_Admin)
# admin.site.register(csv_appstat, csv_appstat_Admin)
# admin.site.register(csv_officers, csv_officers_Admin)
# admin.site.register(csv_docs, csv_docs_Admin)
# admin.site.register(csv_templates, csv_templates_Admin)
# admin.site.register(csv_industry, csv_industry_Admin)
# admin.site.register(csv_stages, csv_stages_Admin)
# admin.site.register(csv_clientfile, csv_clientfile_Admin)



