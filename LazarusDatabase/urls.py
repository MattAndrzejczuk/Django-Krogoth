from django.conf.urls import url, include
from LazarusDatabase import views
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, FeatureTDF
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Mods', views.TotalAnnihilationModViewset)
router.register(r'LazarusModProject', views.LazarusModProjectViewset)
router.register(r'LazarusModAsset', views.LazarusModAssetViewset)
router.register(r'LazarusModDependency', views.LazarusModDependencyViewset)
router.register(r'LazarusPublicAssets', views.LazarusPublicAssetsViewset)
router.register(r'SelectedAssetUploadRepository', views.SelectedAssetUploadRepositoryViewset)
router.register(r'Upload', views.HPIUploadViewset)


urlpatterns = [
    url(r'^TotalAnnihilation/', include(router.urls)),

    url(r'^CommanderAccount/', views.CommanderAccountView.as_view(), name='Commander Account'),
    url(r'^SelectedAssetRepo/', views.SelectedAssetRepo.as_view(), name='Selected Asset Repo'),
    url(r'^SelectedModProjectsList/', views.SelectedModProjectsList.as_view(), name='Selected Mod Projects'),
    url(r'^SelectedModProject/', views.SelectedModProject.as_view(), name='Currently Selected Mod Project'),
    url(r'^UnitFBIFromSQLView/', views.UnitFBIFromSQLView.as_view(), name='UnitFBIFromSQL'),
    url(r'^WeaponTDFFromSQLView/', views.WeaponTDFFromSQLView.as_view(), name='WeaponTDFFromSQL'),
    url(r'^DownloadTDFFromSQLView/', views.DownloadTDFFromSQLView.as_view(), name='DownloadTDFFromSQLView'),
    url(r'^FeatureTDFFromSQLView/', views.FeatureTDFFromSQLView.as_view(), name='FeatureTDFFromSQLView'),
    url(r'^rawDependencyAsTextView/', views.rawDependencyAsTextView.as_view(), name='rawDependencyAsTextView'),
]
