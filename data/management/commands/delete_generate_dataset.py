from django.core.management.base import BaseCommand
from data.models import DatasetGenerate

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        DatasetGenerate.objects.all().delete()
        print("GenerateDataset hamash delete shod")