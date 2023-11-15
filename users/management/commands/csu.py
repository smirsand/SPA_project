import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс нового пользователя со всеми правами.
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('EMAIL_USER'),
            first_name=os.getenv('FIRST_NAME'),
            last_name=os.getenv('LAST_NAME'),
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(os.getenv('PASSWORD_USER'))
        user.save()
