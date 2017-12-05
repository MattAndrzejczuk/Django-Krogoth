from django.contrib import admin

# Register your models here.
from LazarusIV.models import UploadRepository, BackgroundWorkerJob, RepositoryDirectory, RepositoryFile, \
    NotificationCenter, NotificationItem

class UploadRepositoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'root_path', 'original_hpi_path' )

class BackgroundWorkerJobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'id', 'is_finished', 'is_working' )

class RepositoryDirectoryAdmin(admin.ModelAdmin):
    list_display = ('dir_name', 'id', 'dir_path', 'dir_total_files' )

class RepositoryFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'id', 'file_path', 'file_thumbnail', 'file_kind', )

class NotificationCenterAdmin(admin.ModelAdmin):
    list_display = ('unread_private', 'id', )

class NotificationItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date', 'unread', )

admin.site.register(UploadRepository, UploadRepositoryAdmin)
admin.site.register(BackgroundWorkerJob, BackgroundWorkerJobAdmin)
admin.site.register(RepositoryDirectory, RepositoryDirectoryAdmin)
admin.site.register(RepositoryFile, RepositoryFileAdmin)
admin.site.register(NotificationCenter, NotificationCenterAdmin)
admin.site.register(NotificationItem, NotificationItemAdmin)

from LazarusIV.models_tdf import LazarusDamageDataTA, LazarusDownloadDataTA, LazarusUnitDataTA,\
    LazarusFeatureDataTA, LazarusWeaponDataTA

class LazarusUnitDataTAAdmin(admin.ModelAdmin):
    list_display = ('Name', 'UnitName', 'id', 'MaxDamage',)

class LazarusWeaponDataTAAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'rendertype', 'explosionart', 'energypershot', 'id', )

class LazarusDamageDataTAAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'damage_amount',)

class LazarusFeatureDataTAAdmin(admin.ModelAdmin):
    list_display = ('category','description','footprintx','energy','metal')

class LazarusDownloadDataTAAdmin(admin.ModelAdmin):
    list_display = ('UNITNAME', 'UNITMENU',)

admin.site.register(LazarusUnitDataTA, LazarusUnitDataTAAdmin)
admin.site.register(LazarusWeaponDataTA, LazarusWeaponDataTAAdmin)
admin.site.register(LazarusFeatureDataTA, LazarusFeatureDataTAAdmin)
admin.site.register(LazarusDownloadDataTA, LazarusDownloadDataTAAdmin)
admin.site.register(LazarusDamageDataTA, LazarusDamageDataTAAdmin)