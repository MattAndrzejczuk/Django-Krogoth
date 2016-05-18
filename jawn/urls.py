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
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from chat.views import *
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'jawn-users', JawnUserViewSet)
router.register(r'image-messages', ImageMessageViewSet)
router.register(r'text-messages', TextMessageViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'private-message-relationships', PrivateMessageRelationshipSet)
router.register(r'regions', RegionViewSet, base_name="Region")

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
