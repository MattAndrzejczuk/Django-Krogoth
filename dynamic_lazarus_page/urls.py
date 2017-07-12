from django.conf.urls import url
from dynamic_lazarus_page import views

from dynamic_lazarus_page.views import SampleAPI, CustomHtmlGenerator, DynamicIndexModule, SuperBasicModelView, \
    AngularFuseApplicationView, FuseAppComponentView, DynamicJavaScriptInjector, DynamicHTMLInjector, \
    DynamicIndexRoute, NgIncludedHtmlView, DynamicHTMLToolbarView, DynamicHTMLSubNavbarView, \
    DynamicHTMLMainNavbarView, DynamicSplashScreenView, OpenTADataFile



urlpatterns = [
    url(r'^sample_api/', SampleAPI.as_view(), name='sample API'),
    url(r'^sample_html/', CustomHtmlGenerator.as_view(), name='sample HTML'),
    url(r'^DynamicIndexModule/', DynamicIndexModule.as_view(), name='DynamicIndexModule'),
    url(r'^DynamicIndexRoute/', DynamicIndexRoute.as_view(), name='DynamicIndexRoute'),

    url(r'^DynamicHTMLToolbar/', DynamicHTMLToolbarView.as_view(), name=''),
    url(r'^DynamicHTMLMainNavbar/', DynamicHTMLMainNavbarView.as_view(), name=''),
    url(r'^DynamicHTMLSubNavbar/', DynamicHTMLSubNavbarView.as_view(), name=''),
    url(r'^DynamicSplashScreen/', DynamicSplashScreenView.as_view(), name=''),

    url(r'^OpenTADataFile/', OpenTADataFile.as_view(), name='OpenTADataFile'),
## OpenTADataFile

    url(r'^DynamicJavaScriptInjector/', DynamicJavaScriptInjector.as_view(), name='DynamicJavaScriptInjector'),
    url(r'^DynamicHTMLInjector/', DynamicHTMLInjector.as_view(), name='DynamicHTMLInjector'),

    url(r'^SuperBasicModelView/', SuperBasicModelView.as_view(), name='SuperBasicModelView'),

    url(r'^AngularFuseApplication/', AngularFuseApplicationView.as_view(), name='AngularFuseApplication'),
    url(r'^FuseAppComponent/', FuseAppComponentView.as_view(), name='FuseAppComponent'),

    url(r'^NgIncludedHtml/', NgIncludedHtmlView.as_view(), name='NgIncludedHtml'),
]

# DynamicSplashScreen