from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import BlogPost
from .serializer import BlogPostSerializer


# Create your views here.

@api_view()
def api_home(request):
    context = {"greetings": "hello world"}
    return Response(context)


@api_view(['GET', 'POST'])
def blog_posts(request):

    # retrieving all the blog posts.
    if request.method == "GET":
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)
    
    # creating a new blog post.
    elif request.method == "POST":
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET","PUT","DELETE"])
def BlogDetail(request, slug):

    # Check if the blog post exists.
    try:
        blog = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Display the blog
    if request.method == "GET":
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)
    
    # Updating the blog
    elif request.method == "PUT":
        serializer = BlogPostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # deleting a blog
    elif request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)