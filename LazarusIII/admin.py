from django.contrib import admin

# Register your models here.
from LazarusIII.models import LazarusDamageDataTA, LazarusDownloadDataTA, LazarusUnitDataTA,\
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