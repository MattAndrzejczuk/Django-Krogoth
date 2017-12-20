from django.conf.urls import url, include
from CommunityForum import views



urlpatterns = [
    url(r'^ForumCategoryMakeDefaults/', views.ForumCategoryMakeDefaults.as_view(),
        name='Forum Category Make Defaults'),

    url(r'^ForumCategoryListView/', views.ForumCategoryListView.as_view(),
        name='Forum Category List View'),

    url(r'^ForumCategoryDetailView/', views.ForumCategoryDetailView.as_view(),
        name='Forum Category Detail View'),

    url(r'^ForumPostDetailView/', views.ForumPostDetailView.as_view(),
        name='Forum Post Detail View'),

    url(r'^ForumReplySubmitView/', views.ForumReplySubmitView.as_view(),
        name='Forum Reply Submit View'),
]

