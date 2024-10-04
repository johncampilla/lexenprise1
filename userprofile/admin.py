from django.contrib import admin
from . models import *
from casefolder.models import Lawyer_Data
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ['userid','address', 'rank', 'access_code', 'supporto', 'mobile', 'image', 'remarks', 'name', 'date_acquired']

admin.site.register(User_Profile, UserProfileAdmin)
# admin.site.register(Lawyer_Data)
