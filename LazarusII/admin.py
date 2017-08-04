from django.contrib import admin

# Register your models here.
from LazarusII.models import WeaponTDF, Damage, FeatureTDF, UnitFbiData, DownloadTDF, SoundSetTDF




# class StoredFilesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'file_name', 'file_type', 'absolute_path', 'date_logged',)

class WeaponTDFAdmin(admin.ModelAdmin):
    list_display = ('_OBJECT_KEY_NAME', 'name', 'rendertype', 'explosionart', 'energypershot', 'id', )

class DamageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'damage_amount',)

class FeatureTDFAdmin(admin.ModelAdmin):
    list_display = ('category','description','footprintx','energy','metal')

class UnitFbiDataAdmin(admin.ModelAdmin):
    list_display = ('Name', 'id', 'UnitName', 'Builder', 'MaxDamage', 'SoundCategory')

class DownloadTDFAdmin(admin.ModelAdmin):
    list_display = ('UNITNAME', 'parent_unit', 'UNITMENU',)

class SoundTDFAdmin(admin.ModelAdmin):
    list_display = ('_OBJECT_KEY_NAME', 'id', 'select1', 'ok1', 'cant1',)




# admin.site.register(StoredFiles, StoredFilesAdmin)

admin.site.register(WeaponTDF, WeaponTDFAdmin)
admin.site.register(Damage, DamageAdmin)
admin.site.register(FeatureTDF, FeatureTDFAdmin)
admin.site.register(UnitFbiData, UnitFbiDataAdmin)
admin.site.register(DownloadTDF, DownloadTDFAdmin)
admin.site.register(SoundSetTDF, SoundTDFAdmin)


