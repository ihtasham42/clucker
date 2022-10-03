from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import Post, User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "@johndoe",
            first_name = "John",
            last_name="Doe",
            email="johndoe@example.org",
            password="Password123",
            bio="The quick brown fox jumps over the lazy dog"
        )

    def test_valid_user(self):
        self._assert_user_is_valid()
        
    def test_username_cannot_be_blank(self):
        self.user.username = ""
        self._assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = "@" + "a" * 29
        self._assert_user_is_valid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail("Test user should be valid")

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "@johndoe",
            first_name = "John",
            last_name="Doe",
            email="johndoe@example.org",
            password="Password123",
            bio="The quick brown fox jumps over the lazy dog"
        )
        self.post1 = Post(author=self.user, text="This is a test post.")
        self.post2 = Post(author=self.user, text="This is another test post.")

    def test_valid_post(self):
        try:
            self.post1.full_clean()
        except (ValidationError):
            self.fail("Test post should be valid")

    def test_first_post(self):
        queried_post = Post.objects.all().first()
        self.assertEquals(queried_post, self.post2.pk)

    