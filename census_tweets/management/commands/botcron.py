from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        management.call_command("gettweets")
        management.call_command("maketweets")
