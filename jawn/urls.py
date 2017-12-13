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
from filebrowser.sites import site
from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from chat.views import UserViewSet, JawnUserViewSet, ImageMessageViewSet, TextMessageViewSet, ChannelViewSet, \
    MessageViewSet, PrivateMessageRelationshipSet, RegionViewSet, LinkMessageViewSet, YouTubeMessageViewSet
from django.contrib import admin
# from rest_auth.views import LazarusListUnits
from rest_auth.views import index

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


urlpatterns = [

    url(r'^admin_a9k/', admin.site.urls),

    url(r'^$', index),

    url(r'^LazarusIV/', include('LazarusIV.urls')),
    url(r'^LazarusV/', include('LazarusV.urls')),



    url(r'^dynamic_lazarus_page/', include('dynamic_lazarus_page.urls')),
    url(r'^Djangular/', include('Djangular.urls')),
    url(r'^Forum/', include('CommunityForum.urls')),


    # user auth, forgot_password, reset pass, etc..
    url(r'^api/', include(router.urls)),
    # url(r'^api/channel-list/', ChannelList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts/', include('allauth.urls')),


    # Admin stuff
    url(r'^djangular_dashboard/', include('djangular_dashboard.urls')),
    url(r'^admin_a9k/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

]
