from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import User

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
        self._assert_user_is_valid(self.user)

        
    def test_username_cannot_be_blank(self):
        self.user.username = ""
        self._assert_user_is_invalid(self.user)

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