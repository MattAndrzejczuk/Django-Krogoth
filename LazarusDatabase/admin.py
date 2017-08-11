from django.contrib import admin

# Register your models here.
from LazarusDatabase.models import LazarusModProject, LazarusModAsset, LazarusModDependency




class LazarusModProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'developer')

class LazarusModAssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'project_id')

class LazarusModDependencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'system_path', 'asset_id')



admin.site.register(LazarusModProject, LazarusModProjectAdmin)
admin.site.register(LazarusModAsset, LazarusModAssetAdmin)
admin.site.register(LazarusModDependency, LazarusModDependencyAdmin)


