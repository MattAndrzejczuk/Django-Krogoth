from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from krogoth_social.views import AKThreadViewSet, AKThreadCategoryViewSet, AKThreadSocialMediaViewSet, AKThreadListView, update_thread_moddate, AKThreadSocialMediaReplyViewSet

# AKThreadSocialMediaViewSet


router = DefaultRouter()
# router.register(r'AKThreadListView', AKThreadListView, 'AKThreadListView')
router.register(r'AKThread', AKThreadViewSet, 'AKThreadViewSets')
router.register(r'AKThreadCategory', AKThreadCategoryViewSet, 'AKThreadCategoryViewSet')
router.register(r'AKThreadSocialMedia', AKThreadSocialMediaViewSet, 'AKThreadSocialMediaViewSet')
router.register(r'AKThreadSocialMediaReply', AKThreadSocialMediaReplyViewSet, 'AKThreadSocialMediaReply')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^AKThreadListView/$', AKThreadListView.as_view()),
    url(r'^update_thread_moddate/$', update_thread_moddate.as_view()),
]
