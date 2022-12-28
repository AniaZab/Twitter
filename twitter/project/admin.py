from django.contrib import admin

from project.models import Post

# Register your models here.

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     fields = ('user') #, 'likedPosts')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('user', 'likedBy', 'title', 'content')
