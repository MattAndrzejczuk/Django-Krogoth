from django.contrib import admin

# Register your models here.
from dynamic_lazarus_page.models import SuperBasicModel, Car, FuseAppComponent, AngularFuseApplication, NgIncludedHtml


class AngularFuseApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'js_controller', 'js_module',)


class FuseAppComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','type','parent_app','contents',)


class NgIncludedHtmlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(AngularFuseApplication, AngularFuseApplicationAdmin)
admin.site.register(FuseAppComponent, FuseAppComponentAdmin)
admin.site.register(NgIncludedHtml, NgIncludedHtmlAdmin)
