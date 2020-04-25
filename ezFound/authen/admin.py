from django.contrib import admin
from account.models import Profile
from authen.models import OTP
from posts.models import Category, Location, Post, PostImage, Message, Comment
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'user', 'phone']
    list_per_page = 10
    # list_filter = ['student_id', 'user', 'phone']
    search_fields = ['student_id']

class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['name']
    list_display = ['name', 'create_at']
    exclude = ['delete_at']

class LocationAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['name']
    list_display = ['name', 'create_at']
    exclude = ['delete_at']

class PostAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['title']
    list_display = ['title', 'user', 'create_at', 'status']
    exclude = ['delete_at', 'create_at']

class CommentAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['user']
    list_display = ['post', 'user', 'create_at']
    exclude = ['delete_at', 'create_at']

class MessageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['send_by']
    list_display = ['post', 'send_by', 'create_at']
    exclude = ['delete_at', 'create_at', 'text', 'is_seen', 'post', 'send_by', 'message_to']

class PostimgAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['post']
    list_display = ['post']
    exclude = ['delete_at', 'create_at']

class OTPAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['user']
    list_display = ['user', 'ref_code', 'otp_code', 'create_at', 'expire_at']
    exclude = ['ref_code', 'otp_code', 'create_at', 'expire_at', 'user']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(OTP, OTPAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostimgAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)