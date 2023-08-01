from django.core.management.base import BaseCommand
from data.models import Dataset


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Dataset.objects.all().delete()
        print("base dataset hamash delete shod")