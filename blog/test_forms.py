from django.test import TestCase, Client
from blog.forms import BlogPostForm, CommentForm
from django.contrib.auth.models import User


class TestBlogForms(TestCase):

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

    def test_post_form(self):
        self.client.login(
            username="testadmin", password="testadminpassword")

        form = BlogPostForm({
            "title": "Test Post",
            "body": "Test post content",
        })
        self.assertTrue(form.is_valid())

    def test_comment_form(self):
        self.client.login(
            username="testuser", password="testpassword")
        form = CommentForm({
            "comment": "Test comment",
        })
        self.assertTrue(form.is_valid())
