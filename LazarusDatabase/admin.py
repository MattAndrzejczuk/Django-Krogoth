from django.contrib import admin

# Register your models here.
from LazarusDatabase.models import LazarusModProject, LazarusModAsset, \
    LazarusModDependency, SelectedAssetUploadRepository




class LazarusModProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)

class LazarusModAssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'project_id')

class LazarusModDependencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'system_path', 'asset_id')

class SelectedAssetUploadRepositoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(LazarusModProject, LazarusModProjectAdmin)
admin.site.register(LazarusModAsset, LazarusModAssetAdmin)
admin.site.register(LazarusModDependency, LazarusModDependencyAdmin)

admin.site.register(SelectedAssetUploadRepository, SelectedAssetUploadRepositoryAdmin)


