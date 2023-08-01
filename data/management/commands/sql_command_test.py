from django.core.management.base import BaseCommand
from data.models import Dataset, DatasetGenerate
from django.db import connection
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # table_name = Dataset.objects.model._meta.db_table
        # raw_query = f'select count(*) from (SELECT  bank_id,COUNT(*) FROM {table_name} group by bank_id) as t'
        # cursor = connection.cursor()
        # cursor.execute(raw_query)
        # print(cursor.fetchall())
        table_name = Dataset.objects.model._meta.db_table
        raw_query = f'select sum(count) AS count, dest_wallet_id, transaction_type, wallet_nickname, sum(transaction_cost) AS transaction_cost, sum(transaction_value) AS transaction_value from {table_name} group by dest_wallet_id, transaction_type, wallet_nickname'
        cursor = connection.cursor()
        cursor.execute(raw_query)
        print(cursor.fetchall())
        print("hi")
        print(Dataset.objects.filter(dest_wallet_id=16777216, transaction_type=27738, wallet_nickname="b5b95e1e98d5746").values())
    def test_generate_400k(self):
        # raw_query1 = f' select t.time, t.count, t.dest_wallet_id, t.transaction_type, t.transaction_type_chain, t.wallet_nickname, t.transaction_cost, t.transaction_value, t.bank_id, t.transaction_gateway_id from (select ROW_NUMBER() OVER() AS num_row,* from {table_name}) as t where num_row={num_row}'
        # raw_query2 = f' select t.time, t.count, t.dest_wallet_id, t.transaction_type, t.transaction_type_chain, t.wallet_nickname, t.transaction_cost, t.transaction_value, t.bank_id, t.transaction_gateway_id from (select ROW_NUMBER() OVER() AS num_row,* from {table_name}) as t where num_row={num_row+1}'

        table_name = Dataset.objects.model._meta.db_table
        result = []
        for _ in range(40000):
            num_row = randrange(1, 1000000)
            raw_query = f' select t.time, t.count, t.dest_wallet_id, t.transaction_type, t.transaction_type_chain, t.wallet_nickname, t.transaction_cost, t.transaction_value, t.bank_id, t.transaction_gateway_id from (select ROW_NUMBER() OVER() AS num_row,* from {table_name}) as t where num_row={num_row}'
            cursor = connection.cursor()
            cursor.execute(raw_query)
            result.append(cursor.fetchall())

        print(result)
    def test_generate_400k2(self):
        #Dataset.objects.to_csv('test.csv')
        table_name = Dataset.objects.model._meta.db_table
        num_row1 = randrange(1, 1000000)
        num_row2 = randrange(1, 1000000)
        #a = Dataset.objects.raw(f' select t.time, t.count, t.dest_wallet_id, t.transaction_type, t.transaction_type_chain, t.wallet_nickname, t.transaction_cost, t.transaction_value, t.bank_id, t.transaction_gateway_id from (select ROW_NUMBER() OVER() AS num_row,* from {table_name}) as t where num_row>{min(num_row1, num_row2)} and num_row<{max(num_row1, num_row2)}')

        b = Dataset.objects.filter().values()[:9]
        # things mishe khoriji b

        c = DatasetGenerate.objects.create(**b[0])

