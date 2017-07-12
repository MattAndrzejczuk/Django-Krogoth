from django.conf.urls import url
from PhotoGalleryManager.views import ScaffoldView, GalleryItemList, GalleryItemDetail, GalleryCollectionList


# PhotoGalleryManager

urlpatterns = [
    url(r'^ScaffoldView/', ScaffoldView.as_view(), name='ScaffoldView'),

    url(r'^GalleryCollectionList/', GalleryCollectionList.as_view(), name='GalleryCollectionList'),

    url(r'^GalleryItemList/', GalleryItemList.as_view(), name='GalleryItemList'),
    url(r'^GalleryItemDetail/', GalleryItemDetail.as_view(), name='GalleryItemDetail'),
]
