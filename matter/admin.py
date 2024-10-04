from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class MatterAdmin(ImportExportModelAdmin):
    list_per_page = 6
    list_max_show_all = 6
    list_display = ['folder','matter_title','application_no','application_date','TM_Image']

class DueDateAdmin(ImportExportModelAdmin):
    list_per_page = 6
    list_max_show_all = 6

    list_display = ['matter','duecode','duedate','particulars','date_complied']


admin.site.register(Matters, MatterAdmin)
admin.site.register(Matter_Applicant)
admin.site.register(Applicant)
admin.site.register(IP_Matter)
admin.site.register(Matter_ClassOfGoods)
admin.site.register(Inventor)
admin.site.register(Matter_Inventor)
admin.site.register(AppDueDate, DueDateAdmin)
admin.site.register(CaseEvidence)
admin.site.register(CaseDescription)
admin.site.register(ConventionPriority)
admin.site.register(IP_MatterImage)
admin.site.register(SelectMatters)
admin.site.register(MatterLitigation)
