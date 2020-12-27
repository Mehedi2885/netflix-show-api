from django.contrib import admin
from .models import MovieShow
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(MovieShow)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('show_id',)
