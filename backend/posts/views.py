from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import User
from .serializers import *


from .models import BlogPost

# Create your views here.


@api_view(['GET'])
def users_list(request):
    data=User.objects.all()
    serializer= UserSerializer(data, context={'request': request}, many =True)

    return  Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    # data=User.ojects.all()
    serializer= UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'PUT'])
def  user_action(request, user_id):
    if request.method == 'DELETE':
        user = User.objects.get(pk=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------------------------------------------------------

@api_view(['GET'])
def post_list(request):
    data=BlogPost.objects.all()
    serializer= BlogPostSerializer(data, context={'request': request}, many =True)
    return  Response(serializer.data)

@api_view(['POST'])
def add_post(request):
    serializer= BlogPostSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT'])
def  post_action(request, post_id):
    if request.method == 'DELETE':
        post = BlogPost.objects.get(pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        post = BlogPost.objects.get(pk=post_id)
        serializer = BlogPostSerializer(post, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# change -------------------------------------------------------------------------------------------

@api_view(['GET'])
def post_list(request):
    data=BlogPost.objects.all()
    serializer= BlogPostSerializer(data, context={'request': request}, many =True)
    return  Response(serializer.data)

@api_view(['POST'])
def add_post(request):
    serializer= BlogPostSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT'])
def  post_action(request, post_id):
    if request.method == 'DELETE':
        post = BlogPost.objects.get(pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        post = BlogPost.objects.get(pk=post_id)
        serializer = BlogPostSerializer(post, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
