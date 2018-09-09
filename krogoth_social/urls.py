


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from krogoth_social.views import AKThreadViewSet, AKThreadCategoryViewSet, AKThreadSocialMediaViewSet, AKThreadListView, \
    update_thread_moddate, AKThreadSocialMediaReplyViewSet, manual_post_method, \
    manual_post_reply, ForumThreadCategoryViewSet, ForumThreadOPViewSet, ForumThreadReplyViewSet

# AKThreadSocialMediaViewSet


router = DefaultRouter()
# router.register(r'AKThreadListView', AKThreadListView, 'AKThreadListView')
router.register(r'AKThread', AKThreadViewSet, 'AKThreadViewSets')
router.register(r'AKThreadCategory', AKThreadCategoryViewSet, 'AKThreadCategoryViewSet')
router.register(r'AKThreadSocialMedia', AKThreadSocialMediaViewSet, 'AKThreadSocialMediaViewSet')
router.register(r'AKThreadSocialMediaReply', AKThreadSocialMediaReplyViewSet, 'AKThreadSocialMediaReply')

router.register(r'ForumThreadCategory', ForumThreadCategoryViewSet, 'Forum Thread Category')
router.register(r'ForumThreadOP', ForumThreadOPViewSet, 'Forum Thread OP')
router.register(r'ForumThreadReply', ForumThreadReplyViewSet, 'Forum Thread Reply')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^AKThreadListView/$', AKThreadListView.as_view()),
    url(r'^manual_post_method/$', manual_post_method.as_view()),
    url(r'^manual_post_reply/$', manual_post_reply.as_view()),
]
