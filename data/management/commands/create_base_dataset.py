from django.core.management.base import BaseCommand
from data.models import Dataset

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        insert_count = Dataset.objects.from_csv('./tranasaction_dataset.csv')
        print(f"{insert_count} records inserted")

