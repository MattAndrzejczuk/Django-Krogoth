from django.contrib import admin

# Register your models here.
from LazarusII.models import WeaponTDF, Damage, FeatureTDF, UnitFbiData, DownloadTDF, StoredFiles




class StoredFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'file_type', 'absolute_path', 'date_logged',)

class WeaponTDFAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rendertype', 'explosionart', 'energypershot',)

class DamageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'damage_amount',)

class FeatureTDFAdmin(admin.ModelAdmin):
    list_display = ('category','description','footprintx','energy','metal')

class UnitFbiDataAdmin(admin.ModelAdmin):
    list_display = ('Name', 'UnitName', 'Builder', 'MaxDamage', 'SoundCategory')

class DownloadTDFAdmin(admin.ModelAdmin):
    list_display = ('UNITNAME', 'parent_unit', 'UNITMENU',)




admin.site.register(StoredFiles, StoredFilesAdmin)

admin.site.register(WeaponTDF, WeaponTDFAdmin)
admin.site.register(Damage, DamageAdmin)
admin.site.register(FeatureTDF, FeatureTDFAdmin)
admin.site.register(UnitFbiData, UnitFbiDataAdmin)
admin.site.register(DownloadTDF, DownloadTDFAdmin)

