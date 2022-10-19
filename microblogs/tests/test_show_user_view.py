from django.urls import reverse
from django.test import TestCase
from microblogs.models import User 
from django.core.exceptions import ObjectDoesNotExist

class ShowUserViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="@johndoe",
            first_name="John",
            last_name="Doe",
            bio="Hello, I am John Doe",
            password="Password123",
            is_active=True
        )

    def test_get_show_user(self):
        url = reverse("show_user", args=[self.user.pk])
        request = self.client.get(url)
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, "show_user.html")
        self.assertEqual(self.user.username, request.context["profile_user"].username)


    def test_show_non_existent_user(self):
        url = reverse("show_user", args=["10"])
        try:
            self.client.get(url)
            self.fail()
        except (ObjectDoesNotExist):
            pass
