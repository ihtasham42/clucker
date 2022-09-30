from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField()

    username = models.CharField(
        max_length=30, 
        unique=True, 
        validators=[RegexValidator(
            regex='r^@\w{3,}$',
            message="Username must consist of @ followed by at least three alphanumericals"
        )]
    )

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(max_length=520, blank=True)