from django.urls import path
from . import views
from .views import PostListView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', PostListView.as_view(), name='blogHome'),
    path('post/<int:pk>', PostDetailView.as_view(), name='postDetail'),
    path('post/new', CreatePostView.as_view(), name='postCreate'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='postUpdate'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='postDelete'),
    path('about/', views.about, name='blogAbout'),

]
