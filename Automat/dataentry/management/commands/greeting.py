from django.core.management.base import BaseCommand

# Propose command = python manage.py greeting <Name>
# Propose output = Hello {name}, good morning!
class Command(BaseCommand):

    # Description info.
    help = "Greets the user."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies user name.")

    # Command logic.
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        message = f"Hello {name}, good morning!"
        self.stdout.write(self.style.SUCCESS(message))