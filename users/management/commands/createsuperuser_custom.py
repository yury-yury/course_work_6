from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='superuser@mail.ru',
            first_name='Yury',
            last_name='Yanovsky',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('1234')
        user.save()