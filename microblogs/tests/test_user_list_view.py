from django.test import TestCase
from django.urls import reverse

class UserListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("user_list")

    def test_user_list_url(self):
        self.assertEqual(self.url, "/users/")

    def test_get_user_list(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "user_list.html")
