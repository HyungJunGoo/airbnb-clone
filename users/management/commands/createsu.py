from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'This Command creates many users'

    def handle(self, *args, **options):

        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser("ebadmin", "9h0jun1115@gmail.com", "12")
            self.stdout.write(self.style.SUCCESS(f"Superuser Created!!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Exists!!"))