from django.urls import path

from blog.views import HomeView, AddPostView, PostListView, PostDetailView,AddCommentView

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('add/',AddPostView.as_view(),name='add_post'),
    path('posts/',PostListView.as_view(),name='posts'),
    path('post/<int:id>',PostDetailView.as_view(),name='post_detail'),
    path('post/<int:id>/comment',AddCommentView.as_view(),name='add_comment'),
]