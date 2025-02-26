# views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Like, Post


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the user has already liked the post
    like = Like.objects.filter(post=post, user=request.user).first()

    if like:
        like.delete()  # Unlike the post
    else:
        Like.objects.create(post=post, user=request.user)

    return redirect("post_detail", post_id=post.id)
