from django.contrib import admin
from .models import Category, Location, Post, Comment

# Register your models here.

class CategoryDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'delete_at']
    search_fields = ['name']

admin.site.register(Category, CategoryDetailAdmin)

admin.site.register(Location)

class PostDetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'date', 'user_id', 'location_id']
    list_filter = ['category_id']

admin.site.register(Post, PostDetailAdmin)

admin.site.register(Comment)