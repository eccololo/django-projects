from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):

    help = "It inserts data to database."

    def handle(self, *args, **kwargs):

        dataset = [
            {"roll_no": 102, "name": "Kola", "age": 47},
            {"roll_no": 103, "name": "Kate", "age": 27},
            {"roll_no": 104, "name": "Jack", "age": 55},
            {"roll_no": 105, "name": "Joseph", "age": 18},
            {"roll_no": 106, "name": "Katia", "age": 30}
        ]
        for data in dataset:
            
            # We don't duplicate data in DB.
            roll_no = data['roll_no']
            existing_data_entry = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existing_data_entry:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f"Student with roll no {roll_no} already exists in DB."))
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))