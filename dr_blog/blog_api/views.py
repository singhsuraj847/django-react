from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, DjangoModelPermissions, BasePermission, SAFE_METHODS
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     def get_queryset(self):
#         return Post.objects.all()


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

# class PostDetail(generics.ListAPIView):
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         slug = self.request.query_params.get('slug', None)
#         return Post.objects.filter(slug=slug)


class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


# class CreatePost(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

class CreatePost(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
