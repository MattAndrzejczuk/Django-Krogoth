from django.contrib import admin
from krogoth_gantry.models.forum_models import ForumThreadCategory, ForumThreadOP, \
    ForumThreadReply
#
#



class AKThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ('uid','title','is_deleted')
    
class AKThreadAdmin(admin.ModelAdmin):
    list_display = ('uid','title','author','pub_date', 'is_deleted')

class AKThreadSocialMediaAdmin(admin.ModelAdmin):
    list_display = ('uid','title','author','date_modified', 'is_deleted')


class ForumThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ('uid', 'weight', 'title',)

class ForumThreadOPAdmin(admin.ModelAdmin):
    list_display = ('uid', 'title', 'author', 'date_modified', 'not_deleted',)

class ForumThreadReplyAdmin(admin.ModelAdmin):
    list_display = ('uid', 'author', 'date_modified', 'not_deleted',)

admin.site.register(ForumThreadCategory, ForumThreadCategoryAdmin)
admin.site.register(ForumThreadOP, ForumThreadOPAdmin)
admin.site.register(ForumThreadReply, ForumThreadReplyAdmin)