from django.urls import path, include

from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, 
                    SignUp, UserProfile, EditProfile, toggleFollow, addLike, addComment)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('auth/signup', SignUp.as_view(), name='signup'),
    path('user_profile/<int:pk>', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
]
