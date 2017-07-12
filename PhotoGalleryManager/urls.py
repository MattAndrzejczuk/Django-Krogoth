from django.conf.urls import url
from PhotoGalleryManager.views import ScaffoldView


# PhotoGalleryManager

urlpatterns = [
    url(r'^ScaffoldView/', ScaffoldView.as_view(), name='ScaffoldView'),
]
