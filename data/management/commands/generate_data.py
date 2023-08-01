import random
from io import StringIO
from django.utils import timezone
import pandas as pd
from contextlib import closing
from random import randint
from data.models import Dataset, DatasetGenerate
from django.core.management.base import BaseCommand
from django.core.paginator import Paginator
from django.db.models.functions import TruncMinute, TruncDay, Trunc
from django.db.models import DateTimeField
from datetime import timedelta


import time
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            tmp_time = DatasetGenerate.objects.latest('time_internal').time_internal
            
            time_now = timezone.now().replace(second=0, microsecond=0)
            while time_now - tmp_time > timedelta(minutes=5):
                dt = tmp_time + timedelta(minutes=5)
                result = []
                result.extend(self.generate_400k())
                result.extend(self.generate_100k())
                last_time2 = self.insert_dataset_generate(result, dt)
                tmp_time = DatasetGenerate.objects.latest('time_internal').time_internal
                time_now = timezone.now().replace(second=0, microsecond=0)
            
            while time_now - tmp_time != timedelta(minutes=5):
                time_now = timezone.now()
            
            result = []
            result.extend(self.generate_400k())
            result.extend(self.generate_100k())
            last_time2 = self.insert_dataset_generate(result, time_now)
        
        except:
            dt = timezone.now().replace(second=0, microsecond=0)
            result = []
            result.extend(self.generate_400k())
            result.extend(self.generate_100k())
            last_time2 = self.insert_dataset_generate(result, dt)

                          
    def in_memory_csv(self, data):
        mem_csv = StringIO()
        pd.DataFrame(data).to_csv(mem_csv, index=False)
        mem_csv.seek(0)
        return mem_csv
    def generate_400k(self):
        result = []
        items_per_page = 400
        all_data = Dataset.objects.all()
        paginator = Paginator(all_data, items_per_page)

        for i in range(1000):
            page_number = randint(1, 2499)
            page_data = paginator.get_page(page_number)

            records = page_data.object_list
            records = records.values()

            result.extend(records)

        return result
    def generate_100k(self):
        result = []
        items_per_page = 100
        all_data = Dataset.objects.all()

        random_num1 = randint(1,1000000) % 10000
        random_num2 = randint(1,1000000) % 10000
        min_random = min(random_num1, random_num2)
        max_random = max(random_num1, random_num2)


        all_data = all_data[min_random : max_random]
        paginator = Paginator(all_data, items_per_page)
        #print(max_random , min_random, paginator.num_pages)

        # move in random pages and each iterate generate : items_per_page
        for i in range(1000):
            page_number = randint(1, paginator.num_pages - 1)
            page_data = paginator.get_page(page_number)

            records = page_data.object_list
            records = records.values()

            # just fo shuffle data
            for i in range(10):
                key_list = ["count", "dest_wallet_id", "transaction_type", "wallet_nickname", "transaction_cost", "transaction_value"]
                key_random = random.choice(key_list)
                records[randint(0, 99)][key_random] = records[randint(0, 99)][key_random]

            result.extend(records)

        return result
            # data_dict = {
            #     "time" : records[randint(0,9)]["time"],
            #     "dest_wallet_id" : records[randint(0,9)]["dest_wallet_id"],
            #     "transaction_type" : records[randint(0,9)]["transaction_type"],
            #     "transaction_type_chain" : records[randint(0,9)]["transaction_type_chain"],
            #     "wallet_nickname" : records[randint(0,9)]["wallet_nickname"],
            #     "transaction_cost" : records[randint(0,9)]["transaction_cost"],
            #     "transaction_value" : records[randint(0,9)]["transaction_value"],
            #     "bank_id" : records[randint(0,9)]["bank_id"],
            #     "transaction_gateway_id": records[randint(0,9)]["transaction_gateway_id"],
            # }
    def insert_dataset_generate(self, data, what_time):
        mem_csv = self.in_memory_csv(data)
        with closing(mem_csv) as csv_io:
            map_dict = {
                'count': 'count',
                'dest_wallet_id': 'dest_wallet_id',
                'transaction_type': 'transaction_type',
                'transaction_type_chain': 'transaction_type_chain',
                'wallet_nickname': 'wallet_nickname',
                'transaction_cost': 'transaction_cost',
                'transaction_value': 'transaction_value',
                'bank_id' : 'bank_id',
                'transaction_gateway_id': 'transaction_gateway_id',
            }
            static_map_dict = {
                'time_internal': what_time
            }
            insert_count = DatasetGenerate.objects.from_csv(csv_io, mapping=map_dict, static_mapping=static_map_dict)
        ok_time = what_time
        print(f"{insert_count} records inserted")
        return ok_time
    def test(self):
        # list_400data = []
        # pivet = randint(0, 1000000)
        # table_name = Dataset.objects.model._meta.db_table
        # #dataset = Dataset.objects.filter().values()[:]
        # count = Dataset.objects.count()
        # for i in range(0, 4):
        #     pivet = randint(0, 999999)
        #     tmp = Dataset.objects.raw(f' select t.time, t.count, t.dest_wallet_id, t.transaction_type, t.transaction_type_chain, t.wallet_nickname, t.transaction_cost, t.transaction_value, t.bank_id, t.transaction_gateway_id from (select ROW_NUMBER() OVER() AS num_row,* from {table_name}) as t where num_row = {pivet}')[0]
        #     print(tmp)
        #     #list_400data.append(tmp[0])
        pass
