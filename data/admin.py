from django.contrib import admin
from django.db.models import Value, CharField
from django.db import models
# Register your models here.

from .models import Dataset, DatasetGenerate, DatasetBackup2, DatasetBackup1


class DatasetAdmin(admin.ModelAdmin):
    list_display = ['time_internal', 'count', 'dest_wallet_id', 'transaction_type', 'transaction_type_chain', 'wallet_nickname', 'transaction_cost', 'transaction_value', 'bank_id', 'transaction_gateway_id']

class DatasetBackup(admin.ModelAdmin):
    list_display = ['time_internal', 'count', 'dest_wallet_id', 'transaction_type', 'wallet_nickname', 'transaction_cost', 'transaction_value']

admin.site.register(Dataset, DatasetAdmin)
admin.site.register(DatasetGenerate, DatasetAdmin)
admin.site.register(DatasetBackup1, DatasetBackup)
admin.site.register(DatasetBackup2, DatasetBackup)

