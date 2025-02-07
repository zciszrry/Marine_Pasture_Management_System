from django.contrib import admin
from app01.models import Account,Staff
from import_export.admin import ImportExportModelAdmin
from .resource import StaffResource
# Register your models here.
class AccountManager(ImportExportModelAdmin):
    list_display = ['id','username','password']

    list_display_links = ['id']
    list_filter = ['id']
    search_fields = ['username']
    readonly_fields = ['id']
    # list_editable = ['username']
    list_per_page = 20

admin.site.register(Account,AccountManager)

class StaffManager(ImportExportModelAdmin):
    resource_class = StaffResource
    list_display = ['id','name','position']

    list_display_links = ['name']
    list_filter = ['position']
    search_fields = ['name']
    readonly_fields = ['id']

    list_per_page = 20

admin.site.register(Staff,StaffManager)

