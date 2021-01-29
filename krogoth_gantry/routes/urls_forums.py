

# from django.conf.urls import include
# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from krogoth_gantry.views.forum_views import AKThreadViewSet, AKThreadCategoryViewSet, AKThreadSocialMediaViewSet, AKThreadListView, \
#     AKThreadSocialMediaReplyViewSet, manual_post_method, \
#     manual_post_reply, ForumThreadCategoryViewSet, ForumThreadOPViewSet, ForumThreadReplyViewSet
# router = DefaultRouter()
# router.register(r'AKThread', AKThreadViewSet, 'AKThreadViewSets')
# router.register(r'AKThreadCategory', AKThreadCategoryViewSet, 'AKThreadCategoryViewSet')
# router.register(r'AKThreadSocialMedia', AKThreadSocialMediaViewSet, 'AKThreadSocialMediaViewSet')
# router.register(r'AKThreadSocialMediaReply', AKThreadSocialMediaReplyViewSet, 'AKThreadSocialMediaReply')
# router.register(r'ForumThreadCategory', ForumThreadCategoryViewSet, 'Forum Thread Category')
# router.register(r'ForumThreadOP', ForumThreadOPViewSet, 'Forum Thread OP')
# router.register(r'ForumThreadReply', ForumThreadReplyViewSet, 'Forum Thread Reply')
# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('AKThreadListView/', AKThreadListView.as_view()),
#     path('manual_post_method/', manual_post_method.as_view()),
#     path('manual_post_reply/', manual_post_reply.as_view()),
# ]