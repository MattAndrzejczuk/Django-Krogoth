from django.contrib import admin

# Register your models here.
from DatabaseSandbox.models import VisitorLogSB, LazarusCommanderAccountSB, \
    LazarusModProjectSB, BasicUploadTrackerSB, TotalAnnihilationUploadedFile



class BasicUploadTrackerSBAdmin(admin.ModelAdmin):
    list_display = ('author','file_name','download_url','system_path',)


class LazarusCommanderAccountSBAdmin(admin.ModelAdmin):
    list_display = ('user','faction','about_me','is_suspended','is_terminated',)


class VisitorLogSBAdmin(admin.ModelAdmin):
    list_display = ('http_usr','date_created','remote_addr','http_usr',)


class TotalAnnihilationUploadedFileAdmin(admin.ModelAdmin):
    list_display = ('id','designation','file_name','download_url','system_path', 'file_type','is_public')




admin.site.register(BasicUploadTrackerSB, BasicUploadTrackerSBAdmin)
admin.site.register(VisitorLogSB, VisitorLogSBAdmin)
admin.site.register(LazarusCommanderAccountSB, LazarusCommanderAccountSBAdmin)
admin.site.register(TotalAnnihilationUploadedFile, TotalAnnihilationUploadedFileAdmin)