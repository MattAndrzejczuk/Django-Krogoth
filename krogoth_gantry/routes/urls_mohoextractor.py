from django.urls import path

from krogoth_gantry.views.included_html_js_views import NgIncludedHtmlView, \
    KrogothFoundationView, LoadFileAsBase64View
from krogoth_gantry.views.dj_tmpl_rendered import example_view



#####   THIS WAS FORMALLY URLS_AKTHEMES.PY
urlpatterns = [

    # ✅ /moho_extractor/KrogothFoundation?name=EpicPlanet_1.png
    path('KrogothFoundation/', KrogothFoundationView.as_view(), name='Krogoth Foundation'),
    # ✅ /moho_extractor/NgIncludedHtml?name=EpicPlanet_1.png
    path('NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),
    # ✅ /moho_extractor/LoadFileAsBase64?name=EpicPlanet_1.png
    path('LoadFileAsBase64/', LoadFileAsBase64View.as_view(), name='LoadFileAsBase64'),


    path('example', example_view),


]
