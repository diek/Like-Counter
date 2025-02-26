# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post/<int:post_id>/like/", views.like_post, name="like_post"),
]
