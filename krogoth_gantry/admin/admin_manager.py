from django.contrib import admin
from krogoth_gantry.models.krogoth_manager import UncommitedSQL, KrogothVisitorTracking



# Register your models here.
class UncommitedSQLAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'name', 'krogoth_class', 'has_error', 'status',)
    search_fields = ['name', 'krogoth_class']


class KrogothAppTraceAdmin(admin.ModelAdmin):
    list_display = ('remote_addr','username','date_created','http_user_agent',)
    search_fields = ['remote_addr', 'username']


admin.site.register(UncommitedSQL, UncommitedSQLAdmin)
admin.site.register(KrogothVisitorTracking, KrogothAppTraceAdmin)
