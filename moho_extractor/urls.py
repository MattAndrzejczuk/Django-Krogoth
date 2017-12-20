from django.conf.urls import url

from moho_extractor.views import DynamicIndexModule, \
    DynamicJavaScriptInjector, DynamicHTMLInjector, \
    NgIncludedHtmlView, NgIncludedJsView





urlpatterns = [
    url(r'^DynamicIndexModule/', DynamicIndexModule.as_view(), name='DynamicIndexModule'),

    url(r'^DynamicJavaScriptInjector/', DynamicJavaScriptInjector.as_view(), name='DynamicJavaScriptInjector'),
    url(r'^DynamicHTMLInjector/', DynamicHTMLInjector.as_view(), name='DynamicHTMLInjector'),

    url(r'^NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),
    url(r'^NgIncludedJs/', NgIncludedJsView.as_view(), name='NgIncludedJs'),
]
