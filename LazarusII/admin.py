from django.contrib import admin

# Register your models here.
from LazarusII.models import WeaponTDF, Damage, FeatureTDF, UnitFbiData, DownloadTDF




class WeaponTDFAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendertype', 'explosionart', 'energypershot',)

class DamageAdmin(admin.ModelAdmin):
    list_display = ('name', 'damage_amount',)

class FeatureTDFAdmin(admin.ModelAdmin):
    list_display = ('category','description','footprintx','energy','metal')

class UnitFbiDataAdmin(admin.ModelAdmin):
    list_display = ('Name', 'UnitName', 'Builder', 'MaxDamage', 'SoundCategory')

class DownloadTDFAdmin(admin.ModelAdmin):
    list_display = ('UNITNAME', 'parent_unit', 'UNITMENU',)




admin.site.register(WeaponTDF, WeaponTDFAdmin)
admin.site.register(Damage, DamageAdmin)
admin.site.register(FeatureTDF, FeatureTDFAdmin)
admin.site.register(UnitFbiData, UnitFbiDataAdmin)
admin.site.register(DownloadTDF, DownloadTDFAdmin)
