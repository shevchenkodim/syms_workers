from os import environ as environment
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'This custom command for creating a superuser'

    def handle(self, *args, **options):
        User.objects.create_superuser(
            username=environment['SUPERUSER_USERNAME'],
            email=environment['SUPERUSER_EMAIL'],
            password=environment['SUPERUSER_PASSWORD'],
            first_name=environment['SUPERUSER_FIRSTNAME'],
            last_name=environment['SUPERUSER_LASTNAME'],
        )
