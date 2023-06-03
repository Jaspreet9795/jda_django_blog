from rest_framework import serializers
from .models import User, BlogPostCategory, BlogPost, BlogPostFav, BlogPostLikes, BlogPostTag, Comment, CommentLikes, Inquiry


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','username', 'email', 'password', 'first_name', 'last_name', 'profile_description', 'profile_image')


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model= BlogPost
        fields =('pk', 'title','blog_post_type','expected_read_time','unit_of_time','post_image', 'post_image_link', 'post_video', 'post_video_link', 'post_audio', 'post_audio_link',
                 'content', 'promotion', 'pinned', 'notes', ' comments_enabled', 'post_preview', 'about_the_author', 'slug', 'status', 'post_category', ' post_tag',  'user' )