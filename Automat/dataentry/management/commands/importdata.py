from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv


# Proposed Command - python manage.py importdata file_path
class Command(BaseCommand):

    help = "Imports data from CSV file to DB."

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Specifies path to a CSV file.")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:

                roll_no = row['roll_no']
                existing_data_entry = Student.objects.filter(roll_no=roll_no).exists()

                if not existing_data_entry:
                    #Inserting data to DB. 
                    Student.objects.create(**row)
                else:
                    self.stdout.write(self.style.WARNING(f"Student with roll no {roll_no} already exists in DB."))
        
        self.stdout.write(self.style.SUCCESS("Data imported from CSV file successfully!"))