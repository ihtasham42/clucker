from django.forms import EmailField
from django import forms
from django.test import TestCase
from microblogs.forms import SignUpForm
from microblogs.models import User


class SignUpFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
            "first_name": "Jane",
            "last_name": "Doe",
            "username": "@janedoe",
            "email": "janedoe@gmail.com",
            "bio": "My bio",
            "new_password": "Password123",
            "confirm_password": "Password123"
        }

    def test_valid_sign_up_form(self):
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("username", form.fields)
        self.assertIn("email", form.fields)
        email_field = form.fields["email"]
        self.assertTrue(isinstance(email_field, EmailField))
        self.assertIn("bio", form.fields)
        self.assertIn("new_password", form.fields)
        new_password_widget = form.fields["new_password"].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn("confirm_password", form.fields)
        confirm_password_widget = form.fields["confirm_password"].widget
        self.assertTrue(isinstance(confirm_password_widget, forms.PasswordInput))

    def test_form_uses_model_validation(self):
        self.form_input["username"] = "badusername"
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_uppercase_character(self):
        self.form_input["new_password"] = "password123"
        self.form_input["password_confirmation"] = "password123"
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_lowercase_character(self):
        self.form_input["new_password"] = "PASSWORD123"
        self.form_input["password_confirmation"] = "password123"
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_number(self):
        self.form_input["new_password"] = "passwordABC"
        self.form_input["password_confirmation"] = "password123"
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_new_password_and_password_confirmation_are_indentical(self):
        self.form_input["new_password"] = "SamePassword123"
        self.form_input["password_confirmation"] = "SamePassword123"
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())