from django.contrib import admin

# Register your models here.
from CommunityForum.models import ForumCategory, ForumPost, ForumReply


class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'pub_date')

class ForumReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'pub_date')


admin.site.register(ForumReply, ForumReplyAdmin)
admin.site.register(ForumPost, ForumPostAdmin)
admin.site.register(ForumCategory, ForumCategoryAdmin)
