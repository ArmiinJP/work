from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

from csv import reader
from datetime import datetime

from .models import Dataset
# Create your views here.




def create_base_dataset(request):
# open file in read mode
# {
#     with open('/home/arminjp/Documents/Project/generator/tranasaction_dataset.csv', 'r') as read_obj:
#         csv_reader = reader(read_obj)
#         for row in csv_reader:
#             if row[0] == "time":
#                 print(row)
#                 continue
#             else:
#                 #print(len(row[4]))
#                 if len(row[4]) < 128:      
#                     Dataset.objects.create(
#                         time = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%SZ'),
#                         count = row[1],
#                         dest_wallet_id = row[2],
#                         transaction_type = row[3],
#                         transaction_type_chain = row[4],
#                         wallet_nickname = row[5],
#                         transaction_cost = row[6],
#                         transaction_value = row[7],
#                         bank_id = row[8],
#                         transaction_gateway_id = row[9],
#                     )
#                 #print(Dataset.objects.all())
#                 #break
#         return HttpResponse("dataset ok shod!")
# }
    with open('/home/arminjp/Documents/Project/generator/tranasaction_dataset.csv', 'r') as read_obj:
        Dataset.objects.from_csv(read_obj)

def delete_base_dataset(request):
    Dataset.objects.all().delete()
    return HttpResponse("hameye dataset delete shod!")

def select_sql(request):
    table_name = Dataset.objects.model._meta.db_table
    raw_query = f'SELECT * FROM {table_name}'
    cursor = connection.cursor()
    cursor.execute(raw_query)
    a = cursor.fetchall()
    return HttpResponse(a)
    
def alter_sql(request):
    constrain_name = "data_dataset_time_e744a49e_pk"
    table_name = Dataset.objects.model._meta.db_table
    raw_query = f"ALTER TABLE {table_name} DROP CONSTRAINT {constrain_name}"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    return HttpResponse("ok")