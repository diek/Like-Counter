# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "total_likes",
        "content",
        "created_at",
        "updated_at",
    )
    list_filter = ("author", "created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "created_at")
    list_filter = ("post", "user", "created_at")
    date_hierarchy = "created_at"


# PeanutButter * 12
