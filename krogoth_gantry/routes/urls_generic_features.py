from django.urls import path
from krogoth_gantry.views.other.generic_contact_form import GenericContactViewCreate, GenericContactViewDetail, \
    GenericContactViewListAll


urlpatterns = [
    path('contact/create/', GenericContactViewCreate.as_view()),
    path('contact/list/', GenericContactViewListAll.as_view()),
    path('contact/detail/<int:id>/', GenericContactViewDetail.as_view()),
]
