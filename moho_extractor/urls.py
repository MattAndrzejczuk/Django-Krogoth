from django.conf.urls import url
from moho_extractor.views import NgIncludedHtmlView, KrogothFoundationView, LoadFileAsBase64View







urlpatterns = [

    # ❌
    # url(r'^DynamicIndexModule/', DynamicIndexModule.as_view(), name='DynamicIndexModule'),

    # ❌
    # url(r'^DynamicJavaScriptInjector/', DynamicJavaScriptInjector.as_view(), name='DynamicJavaScriptInjector'),

    # ❌
    # url(r'^DynamicHTMLInjector/', DynamicHTMLInjector.as_view(), name='DynamicHTMLInjector'),

    # ✅
    url(r'^KrogothFoundation/', KrogothFoundationView.as_view(), name='Krogoth Foundation'),

    # ✅
    url(r'^NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),

    # ❌
    # url(r'^NgIncludedJs/', NgIncludedJsView.as_view(), name='NgIncludedJs'),

    # ✅
    url(r'^LoadFileAsBase64/', LoadFileAsBase64View.as_view(), name='LoadFileAsBase64'),
]
