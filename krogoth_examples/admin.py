
from django.contrib import admin
from krogoth_examples.models import Fruit, TextLabel, Manufacturer, Car, Topping, Pizza, Hotel, Occupant, BasicFileUpload, BasicImageUpload


# Register your models here.
class AbstractAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class OccupantAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ['full_name']


class CarAdmin(admin.ModelAdmin):
    list_display = ('model_name',)
    search_fields = ['model_name']


class UploadAdmin(admin.ModelAdmin):
    list_display = ('file',)
    search_fields = ['file']


admin.site.register(Fruit, AbstractAdmin)
admin.site.register(TextLabel, AbstractAdmin)
admin.site.register(Manufacturer, AbstractAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Topping, AbstractAdmin)
admin.site.register(Pizza, AbstractAdmin)
admin.site.register(Hotel, AbstractAdmin)
admin.site.register(Occupant, OccupantAdmin)
admin.site.register(BasicFileUpload, UploadAdmin)
admin.site.register(BasicImageUpload, UploadAdmin)