from django.urls import path
from krogoth_gantry.views.middleware.included_html_js_views import NgIncludedHtmlView, KrogothFoundationView, LoadFileAsBase64View
from krogoth_gantry.views.middleware.legacy_data_views import GenericKGData_GetOneOrCreate, GenericKGData_GetFromCategoryOne
from krogoth_gantry.views.middleware.dj_tmpl_rendered import example_view, load_custom_css, load_krogoth_css, load_background_css, \
    load_core_css, load_core_elements_css





urlpatterns = [

    # ✅
    path('KrogothFoundation/', KrogothFoundationView.as_view(), name='Krogoth Foundation'),
    # ✅
    path('NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),
    # ✅
    path('LoadFileAsBase64/', LoadFileAsBase64View.as_view(), name='LoadFileAsBase64'),


    path('GenericKGData_GetOneOrCreate/', GenericKGData_GetOneOrCreate.as_view(), name='GenericKGData_GetOneOrCreate'),
    path('GenericKGData_GetFromCategoryOne/', GenericKGData_GetFromCategoryOne.as_view(), name='GenericKGData_GetFromCategoryOne'),

    path('example', example_view),

    path('load_custom_css', load_custom_css),
    path('load_krogoth_css', load_krogoth_css),
    path('load_background_css', load_background_css),
    path('load_core_css', load_core_css),
    path('load_core_elements_css', load_core_elements_css),
]
