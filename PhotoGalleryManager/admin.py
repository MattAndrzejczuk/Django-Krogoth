from django.contrib import admin

from PhotoGalleryManager.models import GalleryCollection, GalleryItem
# PhotoGalleryManager



class GalleryCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subheading', 'description', 'unique_name', 'pub_date',)

class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subheading', 'description', 'model_pic', 'pub_date')





admin.site.register(GalleryCollection, GalleryCollectionAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)


