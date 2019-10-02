from django.conf.urls import url
from moho_extractor.views import NgIncludedHtmlView, KrogothFoundationView, LoadFileAsBase64View
from moho_extractor.generic_data_views import GenericKGData_GetOneOrCreate, GenericKGData_GetFromCategoryOne
from moho_extractor.dj_views import example_view, load_custom_css, load_krogoth_css, load_background_css, \
    load_core_css, load_core_elements_css





urlpatterns = [

    # ✅
    url(r'^KrogothFoundation/', KrogothFoundationView.as_view(), name='Krogoth Foundation'),
    # ✅
    url(r'^NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),
    # ✅
    url(r'^LoadFileAsBase64/', LoadFileAsBase64View.as_view(), name='LoadFileAsBase64'),


    url(r'^GenericKGData_GetOneOrCreate/', GenericKGData_GetOneOrCreate.as_view(), name='GenericKGData_GetOneOrCreate'),
    url(r'^GenericKGData_GetFromCategoryOne/', GenericKGData_GetFromCategoryOne.as_view(), name='GenericKGData_GetFromCategoryOne'),

    url(r'^example', example_view),

    url(r'^load_custom_css', load_custom_css),
    url(r'^load_krogoth_css', load_krogoth_css),
    url(r'^load_background_css', load_background_css),
    url(r'^load_core_css', load_core_css),
    url(r'^load_core_elements_css', load_core_elements_css),
]
