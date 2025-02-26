from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Post, Like
from django.urls import reverse


# Test Models
class PostModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email="normal@user.com", password="PeanutButter_22"
        )
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post", author=self.user
        )

    def test_post_creation(self):
        """Test if a post is created correctly"""
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post")
        self.assertEqual(self.post.author.email, "normal@user.com")

    def test_post_str_method(self):
        """Test the __str__ method of Post"""
        self.assertEqual(str(self.post), "Test Post")

    def test_post_total_likes(self):
        """Test total_likes method"""
        self.assertEqual(self.post.total_likes(), 0)
        # create an instance of like
        like = Like.objects.create(post=self.post, user=self.user)
        self.assertEqual(self.post.total_likes(), 1)


class LikeModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email="normal@user.com", password="PeanutButter_22"
        )
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post", author=self.user
        )

    def test_like_creation(self):
        """Test if a like is created correctly"""
        like = Like.objects.create(post=self.post, user=self.user)
        self.assertEqual(like.post, self.post)
        self.assertEqual(like.user, self.user)

    def test_duplicate_like(self):
        """Test that a user cannot like the same post twice
        Should raise an IntegrityError because unique_together
        """
        Like.objects.create(post=self.post, user=self.user)
        with self.assertRaises(Exception):
            Like.objects.create(post=self.post, user=self.user)

    def test_total_likes_by_user(self):
        pass


# Test Views
class PostViewsTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.client = Client()
        self.user = User.objects.create_user(
            email="normal@user.com", password="PeanutButter_22"
        )
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post", author=self.user
        )

    def test_all_posts_view(self):
        """Test if the all_posts view loads correctly"""
        response = self.client.get(reverse("all_posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/all_posts.html")
        self.assertContains(response, "Test Post")

    def test_like_post_view(self):
        """Test liking a post"""
        self.client.login(
            username="normal@user.com", password="PeanutButter_22"
        )  # Login required
        response = self.client.post(reverse("like_post", args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post_view(self):
        """Test unliking a post"""
        self.client.login(username="normal@user.com", password="PeanutButter_22")
        Like.objects.create(
            post=self.post, user=self.user
        )  # User already liked the post
        response = self.client.post(reverse("like_post", args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(Like.objects.count(), 0)  # Like should be removed

    def test_like_requires_login(self):
        """Test that liking a post requires authentication"""
        pass
