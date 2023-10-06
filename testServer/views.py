from rest_framework import generics,status
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class PostListCreateView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['POST'])
def postUser(request):
    post = PostSerializer(data=request.data)
    if post.is_valid():
        post.save()
        return Response(post.data)
    return Response(post.errors,status=status.HTTP_400_BAD_REQUEST)