from django.contrib import admin
from GeneralWebsiteInfo.models import WebsiteColorTheme, WebsiteLayout, \
    NavigationBar, BootScreenLoader



# GeneralWebsiteInfo



class WebsiteColorThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'css_code',  'enabled',)


class WebsiteLayoutAdmin(admin.ModelAdmin):
    list_display = ('id',  'enabled',)


class NavigationBarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'logo_html_code',  'enabled',)


class BootScreenLoaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'html_code',  'enabled',)








admin.site.register(WebsiteColorTheme, WebsiteColorThemeAdmin)
admin.site.register(WebsiteLayout, WebsiteLayoutAdmin)
admin.site.register(NavigationBar, NavigationBarAdmin)
admin.site.register(BootScreenLoader, BootScreenLoaderAdmin)