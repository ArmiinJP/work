from django.core.management.base import BaseCommand
from data.models import Dataset, DatasetGenerate, DatasetBackup2, DatasetBackup1
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.datasetdrop()
        self.datasetgeneratedrop()
        self.backupdata1drop()
        self.backupdata2drop()
    def datasetdrop(self):
        #constrain_name = 'data_dataset_time_e744a49e_pk'
        constrain_name = 'data_dataset_pkey'
        table_name = Dataset.objects.model._meta.db_table
        raw_query = f"ALTER TABLE {table_name} DROP CONSTRAINT {constrain_name}"
        cursor = connection.cursor()
        cursor.execute(raw_query)

    def datasetgeneratedrop(self):
        constrain_name = 'data_datasetgenerate_pkey'
        table_name = DatasetGenerate.objects.model._meta.db_table
        raw_query = f"ALTER TABLE {table_name} DROP CONSTRAINT {constrain_name}"
        cursor = connection.cursor()
        cursor.execute(raw_query)

    def backupdata1drop(self):
        constrain_name = 'data_datasetbackup1_pkey'
        table_name = DatasetBackup1.objects.model._meta.db_table
        raw_query = f"ALTER TABLE {table_name} DROP CONSTRAINT {constrain_name}"
        cursor = connection.cursor()
        cursor.execute(raw_query)

    def backupdata2drop(self):
        constrain_name = 'data_datasetbackup2_pkey'
        table_name = DatasetBackup2.objects.model._meta.db_table
        raw_query = f"ALTER TABLE {table_name} DROP CONSTRAINT {constrain_name}"
        cursor = connection.cursor()
        cursor.execute(raw_query)
