from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
import datetime
import os

# Proposed commmand - python manage.py exportdata <model-name>
class Command(BaseCommand):

    help = "Exports data from database to a CSV file."

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="Model name.")

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        # Search through all models.
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f"Model '{model_name}' not found in any app.")
        else:
              model_data = model.objects.all()


        timestamp = datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
        export_dir = os.path.join(os.getcwd(), "exports")
        
        if not os.path.exists(export_dir):
            os.mkdir(export_dir)

        file_name = f"exported_{model_name}_data_{timestamp}.csv".lower()
        file_path = os.path.join(export_dir, file_name)

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)

            # Writes CSV header
            writer.writerow([field.name for field in model._meta.fields])

            # Writes actual data
            for data in model_data:
                writer.writerow([getattr(data, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS("Data exported to CSV file successfully!"))