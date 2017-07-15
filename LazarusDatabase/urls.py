from django.conf.urls import url
from LazarusDatabase import views
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, FeatureTDF



urlpatterns = [
    url(r'^UnitFBIFromSQLView/', views.UnitFBIFromSQLView.as_view(), name='UnitFBIFromSQL'),
    url(r'^WeaponTDFFromSQLView/', views.WeaponTDFFromSQLView.as_view(), name='WeaponTDFFromSQL'),
    url(r'^DownloadTDFFromSQLView/', views.DownloadTDFFromSQLView.as_view(), name='DownloadTDFFromSQLView'),
    url(r'^FeatureTDFFromSQLView/', views.FeatureTDFFromSQLView.as_view(), name='FeatureTDFFromSQLView'),
]

