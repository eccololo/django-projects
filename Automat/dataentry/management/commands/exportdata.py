from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv
import datetime
import os

# Proposed commmand - python manage.py exportdata
class Command(BaseCommand):

    help = "Exports data from Student model to a CSV file."

    def handle(self, *args, **kwargs):
        students = Student.objects.all()

        timestamp = datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
        export_dir = os.path.join(os.getcwd(), "exports")
        
        if not os.path.exists(export_dir):
            os.mkdir(export_dir)

        file_name = f"exported_students_data_{timestamp}.csv"
        file_path = os.path.join(export_dir, file_name)

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)

            # Writes CSV header
            writer.writerow(['roll_no', 'name', 'age'])

            # Writes actual data
            for student in students:
                writer.writerow([student.roll_no, student.name, student.age])

        self.stdout.write(self.style.SUCCESS("Data exported to CSV file successfully!"))