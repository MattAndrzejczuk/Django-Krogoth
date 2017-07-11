from django.conf.urls import url
from dynamic_lazarus_page import views

from dynamic_lazarus_page.views import SampleAPI, CustomHtmlGenerator, DynamicIndexModule, SuperBasicModelView, \
    AngularFuseApplicationView, FuseAppComponentView, DynamicJavaScriptInjector, DynamicHTMLInjector, \
    DynamicIndexRoute, DynamicHTMLToolbar, NgIncludedHtmlView



urlpatterns = [
    url(r'^sample_api/', SampleAPI.as_view(), name='sample API'),
    url(r'^sample_html/', CustomHtmlGenerator.as_view(), name='sample HTML'),
    url(r'^DynamicIndexModule/', DynamicIndexModule.as_view(), name='DynamicIndexModule'),
    url(r'^DynamicIndexRoute/', DynamicIndexRoute.as_view(), name='DynamicIndexRoute'),
    url(r'^DynamicHTMLToolbar/', DynamicHTMLToolbar.as_view(), name='DynamicHTMLToolbar'),

    url(r'^DynamicJavaScriptInjector/', DynamicJavaScriptInjector.as_view(), name='DynamicJavaScriptInjector'),
    url(r'^DynamicHTMLInjector/', DynamicHTMLInjector.as_view(), name='DynamicHTMLInjector'),

    url(r'^SuperBasicModelView/', SuperBasicModelView.as_view(), name='SuperBasicModelView'),

    url(r'^AngularFuseApplication/', AngularFuseApplicationView.as_view(), name='AngularFuseApplication'),
    url(r'^FuseAppComponent/', FuseAppComponentView.as_view(), name='FuseAppComponent'),

    url(r'^NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),
]
