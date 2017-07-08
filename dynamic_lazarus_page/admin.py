from django.contrib import admin

# Register your models here.
from dynamic_lazarus_page.models import SuperBasicModel, Car, FuseAppComponent, AngularFuseApplication


class AngularFuseApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'js_controller', 'js_module',)


class FuseAppComponentAdmin(admin.ModelAdmin):
    list_display = ('name','type','parent_app','contents',)


admin.site.register(AngularFuseApplication, AngularFuseApplicationAdmin)
admin.site.register(FuseAppComponent, FuseAppComponentAdmin)

