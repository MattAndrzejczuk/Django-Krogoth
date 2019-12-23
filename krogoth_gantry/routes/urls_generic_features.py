from django.conf.urls import url
from krogoth_gantry.views.other.generic_contact_form import GenericContactViewCreate, GenericContactViewDetail, \
    GenericContactViewListAll


urlpatterns = [
    url(r'^contact/create/', GenericContactViewCreate.as_view()),
    url(r'^contact/list/', GenericContactViewListAll.as_view()),
    url(r'^contact/detail/(?P<id>.+)/$', GenericContactViewDetail.as_view()),
]
