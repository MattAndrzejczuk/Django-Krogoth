from django.contrib import admin
from krogoth_admin.models import UncommitedSQL



# Register your models here.
class UncommitedSQLAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'name', 'krogoth_class', 'has_error', 'status',)
    search_fields = ['name', 'krogoth_class']


admin.site.register(UncommitedSQL, UncommitedSQLAdmin)