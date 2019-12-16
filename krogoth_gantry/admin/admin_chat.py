from django.contrib import admin

# Register your models here.

from krogoth_gantry.models.models_chat import Channel, Message, JawnUser, TextMessage


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_posted', )


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel', )


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', )


class JawnUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_me', 'faction', )


admin.site.register(Message, MessageAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(JawnUser, JawnUserAdmin)
admin.site.register(TextMessage, TextAdmin)


