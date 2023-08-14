from django.core.management import BaseCommand

from mailing_service.services import send_email


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_email()
