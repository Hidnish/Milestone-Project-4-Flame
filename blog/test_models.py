from django.test import TestCase, Client
from blog.models import BlogPost, Comment
from django.contrib.auth.models import User


class TestBlogModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )
        self.admin = User.objects.create_superuser(
            username='testadmin',
            email='admin@test.com',
            password='testadminpassword'
        )

    def test_blog_post_model(self):
        self.client.login(
            username="testadmin", password="testadminpassword")
        post = BlogPost.objects.create(
            title="Test Post",
            author=self.admin,
            body="Test Content",
        )
        self.assertEqual(str(post), "Test Post")

    def test_comment_model(self):
        self.client.login(
            username="testuser", password="testpassword")
        post = BlogPost.objects.create(
            title="Test post",
            author=self.user,
            body="Test Content",
        )
        comment = Comment.objects.create(
            post=post,
            user=self.user,
            comment="Test Comment",
        )
        self.assertEqual(str(comment), "Comment on post: Test post by testuser")
