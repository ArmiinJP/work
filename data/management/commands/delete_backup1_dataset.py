from django.core.management.base import BaseCommand
from data.models import DatasetBackup1

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        DatasetBackup1.objects.all().delete()
        print("DatasetBackup1 hamash delete shod")