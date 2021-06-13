from .views import PostList, PostDetail, PostListDetailfilter, CreatePost, AdminPostDetail, EditPost, DeletePost
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls

urlpatterns = [
    path('', PostList.as_view(), name='listcreate'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='customsearch'),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/',
         AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
