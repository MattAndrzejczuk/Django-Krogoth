from django.conf.urls import url
from LazarusDatabase import views
from LazarusII.models import UnitFbiData, WeaponTDF, Damage



urlpatterns = [
    url(r'^UnitFBIFromSQLView/', views.UnitFBIFromSQLView.as_view(), name='UnitFBIFromSQL'),
    url(r'^WeaponTDFFromSQLView/', views.WeaponTDFFromSQLView.as_view(), name='WeaponTDFFromSQL'),
    url(r'^DownloadTDFFromSQLView/', views.WeaponTDFFromSQLView.as_view(), name='WeaponTDFFromSQL'),
]

