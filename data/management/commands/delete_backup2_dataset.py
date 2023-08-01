from django.core.management.base import BaseCommand
from data.models import DatasetBackup2

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        DatasetBackup2.objects.all().delete()
        print("DatasetBackup2 hamash delete shod")