from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from blog.models import BlogPost, Comment


class TestBlogPostViews(TestCase):
    """ Test the blog views for all users """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.admin = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@test.com',
            password='adminuserpassword',
        )
        self.post = BlogPost.objects.create(
            title="Test Post",
            author=self.admin,
            body="Test Content"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            comment="Test Comment",
        )
        self.view_blog = reverse("view_blog")
        self.view_post = reverse("view_blog_post",
                                 kwargs={"post_id": self.post.id})

    def test_view_blog_view(self):
        """ Test the view_blog_post view """

        response = self.client.get(self.view_blog)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog.html")
        self.assertTemplateUsed(response, "base.html")

    def test_view_blog_post_view(self):
        """ Test the view_blog_post view"""

        response = self.client.get(self.view_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_post.html")
        self.assertTemplateUsed(response, "base.html")


class TestPostSuperuserViews(TestCase):
    """
    Test the views for superuser to add
    posts, edit posts, and delete posts
    """

    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username='testadmin',
            email='testadmin@test.com',
            password='testadminpassword'
        )
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )
        self.post = BlogPost.objects.create(
            title="Test Post",
            author=self.user,
            body="Test Content",
        )
        self.add_post = reverse("add_blog_post")
        self.edit_post = reverse("edit_blog_post",
                                 kwargs={"post_id": self.post.id})
        self.delete_post = reverse("delete_blog_post",
                                   kwargs={"post_id": self.post.id})
        self.view_blog = reverse("view_blog")
        self.view_post = reverse("view_blog_post",
                                 kwargs={"post_id": self.post.id})

    def test_add_blog_post_not_superuser(self):
        """ Test adding a post without being superuser """

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.add_post)
        self.assertRedirects(response, self.view_blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, only store owners can do that')

    def test_add_blog_post_superuser_GET(self):
        """
        Test the add_post view with GET request
        if the user is a superuser
        """

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.get(self.add_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_blog_post.html")
        self.assertTemplateUsed(response, "base.html")

    def test_add_blog_post_invalid_POST(self):
        """
        Test the add post view with POST method if the user is a superuser
        and the form invalid
        """

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.post(self.add_post, {
            "title": "Test Post",
            "body": "",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Failed to add the post. \
                                Please check the form inputs \
                                are correct and try again.")

    def test_add_blog_post_valid(self):
        """
        Test the add post view with GET method if the user is a superuser
        and the form is valid
        """

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.post(self.add_post, {
            "title": "Test blog post",
            "body": "Test Content"
        })

        post = BlogPost.objects.get(title="Test blog post")

        self.assertEqual(post.body, 'Test Content')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Post has been added to the Blog.")

    def test_edit_blog_post_not_superuser(self):
        """ Test editing a post without being superuser """

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.edit_post)
        self.assertRedirects(response, self.view_blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, only store owners can do that')

    def test_edit_blog_post_superuser_GET(self):
        """
        Test the edit post view with GET method if the user is a superuser
        """

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.get(self.edit_post)
        self.assertEqual(response.context['form'].initial['title'],
                         self.post.title)
        self.assertEqual(response.context['form'].initial['body'],
                         self.post.body)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_blog_post.html")
        self.assertTemplateUsed(response, "base.html")

    def test_edit_blog_post_invalid_GET(self):
        """
        Test the edit post view GET if the user is a superuser
        and form invalid
        """

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.post(self.edit_post, {

        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Failed to edit the post. \
                                Please check the form inputs \
                                are correct and try again.")

    def test_edit_blog_post_valid_POST(self):
        """
        Test the edit post view with POST method if the user is a superuser
        and the form is valid
        """

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.post(self.edit_post, {
            "title": "Test Post",
            "body": "Test Content",
        })
        post = BlogPost.objects.get(id=self.post.id)
        self.assertEqual(post.body, 'Test Content')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Post updated")

    def test_delete_blog_post_not_superuser(self):
        """ Test the delete post view if a user is not a superuser """

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.delete_post)
        self.assertRedirects(response, self.view_blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, only store owners can do that')

    def test_delete_blog_post_superuser(self):
        """ Test the delete post POST function for superuser """

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.post(self.delete_post)
        post = BlogPost.objects.filter(id=self.post.id)
        self.assertFalse(post)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Post deleted")
