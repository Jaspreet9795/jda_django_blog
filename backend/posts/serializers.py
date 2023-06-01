from rest_framework import serializers
from .models import User, BlogPostCategory, BlogPost, BlogPostFav, BlogPostLikes, BlogPostTag, Comment, CommentLikes, Inquiry


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','username', 'email', 'password', 'first_name', 'last_name', 'profile_description', 'profile_image')