from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db import DataError
import csv


# Proposed Command - python manage.py importdata <file_path> <model_name>
class Command(BaseCommand):

    help = "Imports data from CSV file to DB."

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Specifies path to a CSV file.")
        parser.add_argument('model_name', type=str, help="Name of the model.")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        model = None
        # Search for the model across all installed apps.
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f"Model '{model_name}' not found in any app.")
        
        # Gather model field names extept id field.
        model_fiels = [field.name for field in model._meta.fields if field.name != "id"]

        with open(file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            # Gather CSV header field names.
            csv_header = reader.fieldnames

            # Compare CSV header with model field names.
            if csv_header != model_fiels:
                raise DataError(f"CSV file doesn't match with {model_name} table fields!")

            for row in reader:
                # Remove unexpected keys (like BOM) from row
                row = {key.strip('\ufeff'): value for key, value in row.items()}
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS("Data imported from CSV file successfully!"))