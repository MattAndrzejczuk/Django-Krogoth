from django.conf.urls import url, include
from LazarusPublisherTest import views



urlpatterns = [
    url(r'^SerializeFBIFileInPathNoSave/',
        views.SerializeFBIFileInPathNoSave.as_view(),
        name='Serialize FBI File In Path No Save'),
    url(r'^GatherDependenciesForModAssetTestAbel/',
        views.GatherDependenciesForModAssetTestAbel.as_view(),
        name='GatherDependenciesForModAssetTestAbel'),
]

# we need,

# 1.] GET all dependencies for asset with id.
# 2.] Copy the non-editable files to a new dir.
# 3.] Convert JSON Weapon, Unit & Download back into naitive TA data file.
# 4.] Save conversion to new directory.

\