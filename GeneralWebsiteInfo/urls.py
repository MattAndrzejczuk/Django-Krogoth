from django.conf.urls import url
from GeneralWebsiteInfo.views import WebsiteColorThemeView, WebsiteLayoutView, \
    NavigationBarView, BootScreenLoaderView, PressArticleListView, PressArticleView
from django.contrib.auth.models import User




# GeneralWebsiteInfo

###   WebsiteColorTheme
###   WebsiteLayout
###   NavigationBar
###   BootScreenLoader




urlpatterns = [

    url(r'^WebsiteColorTheme/', WebsiteColorThemeView.as_view(), name=' '),
    url(r'^WebsiteLayout/', WebsiteLayoutView.as_view(), name=' '),

    url(r'^NavigationBar/', NavigationBarView.as_view(), name=' '),
    url(r'^BootScreenLoader/', BootScreenLoaderView.as_view(), name='  '),

    url(r'^PressArticleList/', PressArticleListView.as_view(), name='Press Articles'),
    url(r'^PressArticle/', PressArticleView.as_view(), name='Press Article'),
]

