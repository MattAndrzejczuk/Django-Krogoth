from django.contrib import admin
from krogoth_social.models import AKThread, AKThreadCategory, AKThreadSocialMedia
#
#



class AKThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ('uid','title','is_deleted')
    
class AKThreadAdmin(admin.ModelAdmin):
    list_display = ('uid','title','author','pub_date', 'is_deleted')

class AKThreadSocialMediaAdmin(admin.ModelAdmin):
    list_display = ('uid','title','author','date_modified', 'is_deleted')

#
# class ForumPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'pub_date')
#
# class ForumReplyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'body', 'pub_date')
#
#
# admin.site.register(ForumReply, ForumReplyAdmin)
admin.site.register(AKThread, AKThreadAdmin)
admin.site.register(AKThreadCategory, AKThreadCategoryAdmin)


admin.site.register(AKThreadSocialMedia, AKThreadSocialMediaAdmin)