from io import StringIO
import pandas as pd
from contextlib import closing
from data.models import DatasetGenerate, DatasetBackup1
from django.db import models
from django.core.management.base import BaseCommand
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from datetime import timedelta

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        result = self.backup()
        if len(result) == 0:
            print("nothing add")
            return
        self.insert_dataset_generate(result)

    def backup(self):
        try:
            tmp_time1 = DatasetBackup1.objects.latest('time_internal').time_internal
            tmp_time1 = tmp_time1 + timedelta(hours=1)
            tmp_time2 = DatasetGenerate.objects.latest('time_internal').time_internal
            tmp_time2 = tmp_time2.replace(minute=0, second=0, microsecond=0)
             
            results = DatasetGenerate.objects.filter(time_internal__gte=tmp_time1, time_internal__lt=tmp_time2).values('dest_wallet_id', 'transaction_type', 'wallet_nickname').annotate(
                transaction_value=models.Sum('transaction_value')
                ,transaction_cost=models.Sum('transaction_cost')
                ,count=models.Sum('count'),
                time_internal=Trunc('time_internal', 'hour', output_field = DateTimeField()))
        except:
            tmp_time = DatasetGenerate.objects.latest('time_internal').time_internal
            tmp_time = tmp_time.replace(minute=0, second=0, microsecond=0)
            results = DatasetGenerate.objects.filter(time_internal__lt=tmp_time).values('dest_wallet_id', 'transaction_type', 'wallet_nickname').annotate(
                transaction_value=models.Sum('transaction_value')
                ,transaction_cost=models.Sum('transaction_cost')
                ,count=models.Sum('count'),
                time_internal=Trunc('time_internal', 'hour', output_field = DateTimeField()))

        return results

    def insert_dataset_generate(self, data):
        mem_csv = self.in_memory_csv(data)
        with closing(mem_csv) as csv_io:
            insert_count = DatasetBackup1.objects.from_csv(csv_io)
            print(f"{insert_count} records inserted")

    def in_memory_csv(self, data):
        mem_csv = StringIO()
        pd.DataFrame(data).to_csv(mem_csv, index=False)
        mem_csv.seek(0)
        return mem_csv