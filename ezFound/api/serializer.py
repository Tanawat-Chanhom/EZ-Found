from rest_framework import serializers

from django.contrib.auth.models import User

from posts.models import Post, Comment, Message, Location, Category, PostImage
from authen.models import OTP
from account.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'descriptions', 'status', 'date,', 'user', 'category', 'location', 'create_at', 'delete_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'create_at', 'delete_at', 'user', 'post']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'is_seen', 'create_at', 'post', 'send_by', 'message_to']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'create_at', 'delete_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'create_at', 'delete_at']


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image_url', 'create_at', 'delete_at', 'post']


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['ref_code', 'otp_code', 'create_at', 'expire_at', 'user']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['student_id', 'phone', 'information', 'profile_img_path', 'user']

