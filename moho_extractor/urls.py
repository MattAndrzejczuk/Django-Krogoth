from django.conf.urls import url
from moho_extractor.views import NgIncludedHtmlView, KrogothFoundationView, LoadFileAsBase64View







urlpatterns = [

    # ✅
    url(r'^KrogothFoundation/', KrogothFoundationView.as_view(), name='Krogoth Foundation'),

    # ✅
    url(r'^NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),

    # ✅
    url(r'^LoadFileAsBase64/', LoadFileAsBase64View.as_view(), name='LoadFileAsBase64'),
]
