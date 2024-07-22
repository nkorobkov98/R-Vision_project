from django.contrib import admin
from .models import RHBA
from import_export import fields, resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.


class RHBAResource(resources.ModelResource):

    class Meta:
        model = RHBA
        


class RHBAAdmin(ImportExportActionModelAdmin):
    resource_class = RHBAResource
    list_display = [field.name for field in RHBA._meta.fields]
    search_fields = ('CVEs', 'RHBA')


admin.site.register(RHBA, RHBAAdmin)