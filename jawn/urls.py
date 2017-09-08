"""jawn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))



"""
from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from chat.views import *
from django.contrib import admin
# from rest_auth.views import LazarusListUnits
import rest_auth

router = DefaultRouter()
router.register(r'users', UserViewSet, 'User')
router.register(r'jawn-users', JawnUserViewSet, 'Jawn User')
router.register(r'image-messages', ImageMessageViewSet, 'Image Message')
router.register(r'text-messages', TextMessageViewSet, 'Text Message')
router.register(r'channels', ChannelViewSet, 'Channel')
router.register(r'messages', MessageViewSet, 'Message')
router.register(r'private-message-relationships', PrivateMessageRelationshipSet, 'Private Message')
router.register(r'regions', RegionViewSet, 'Region')
router.register(r'link-messages', LinkMessageViewSet)
router.register(r'youtube-messages', YouTubeMessageViewSet)
router.register(r'youtube', YouTubeMessageViewSet)



# LEGACY SUPPORT OF iOS 8 VERSION, THE iOS 8 CLIENT MUST BE UPDATED SO WE CAN REMOVE THIS LINE LATER

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/channel-list/', ChannelList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin_a9k/', admin.site.urls),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^$', rest_auth.views.index),
    url(r'^GooglePlusOAuthCallback', rest_auth.views.GooglePlusOAuthCallbackView.as_view()),
    url(r'^armprime/', rest_auth.views.index),
    # url(r'^lazarus/', LazarusListUnits.as_view()),
    url(r'^api.lazarus/', include('lazarus.urls')),
    url(r'^LazarusII/', include('LazarusII.urls')),
    url(r'^LazarusIII/', include('LazarusIII.urls')),
    url(r'^SandboxDB/', include('DatabaseSandbox.urls')),

    url(r'^dynamic_lazarus_page/', include('dynamic_lazarus_page.urls')),

    url(r'^GeneralWebsiteInfo/', include('GeneralWebsiteInfo.urls')),
    url(r'^PhotoGalleryManager/', include('PhotoGalleryManager.urls')),
    url(r'^LazarusDatabase/', include('LazarusDatabase.urls')),
    url(r'^Djangular/', include('Djangular.urls')),
    url(r'^Forum/', include('CommunityForum.urls')),

    url(r'^djangular_dashboard/', include('djangular_dashboard.urls')),

    url(r'^docs/', include('rest_framework_docs.urls')),
]