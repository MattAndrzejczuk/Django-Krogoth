from django.contrib import admin

# Register your models here.
from LazarusV.models import ModProject, ModPublication, ModBuild, WargamePackage, \
    WargameFile, WargameData

class ModProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_public')

class ModPublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

class ModBuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'download_url', )

class WargamePackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

class WargameFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'unique_name', )

class WargameDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'unique_name', )




admin.site.register(ModProject, ModProjectAdmin)
admin.site.register(ModPublication, ModPublicationAdmin)
admin.site.register(ModBuild, ModBuildAdmin)
admin.site.register(WargamePackage, WargamePackageAdmin)
admin.site.register(WargameFile, WargameFileAdmin)
admin.site.register(WargameData, WargameDataAdmin)