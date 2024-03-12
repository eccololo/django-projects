from django.core.management.base import BaseCommand

class Command(BaseCommand):

    # Help hints for command in terminal
    help = "Prints Hello World string."

    # Command logic method.
    def handle(self, *args, **kwargs):
        self.stdout.write("Hello World")
