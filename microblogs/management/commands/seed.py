from django.core.management.base import BaseCommand, CommandError 
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker("en_GB")

    def handle(self, *args, **options):
        for i in range(100):
            user = User.objects.create_user(
                username="@" + self.faker.first_name() + str(i),
                email=str(i) + self.faker.email(),
                password=self.faker.password(),
                first_name=self.faker.first_name(),
                last_name=self.faker.last_name(),
                bio=self.faker.text()
            )