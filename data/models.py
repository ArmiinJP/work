from django.db import models
from postgres_copy import CopyManager
from django.utils import timezone


class Dataset(models.Model):
    time_internal = models.DateTimeField(primary_key=True)
    count = models.IntegerField()
    dest_wallet_id = models.BigIntegerField()
    transaction_type = models.IntegerField()
    #transaction_type_chain = ArrayField(models.CharField(max_length=128), blank=True)
    transaction_type_chain = models.CharField(max_length=128)
    wallet_nickname = models.CharField(max_length=16, null=True, blank=True)
    transaction_cost = models.BigIntegerField()
    transaction_value = models.BigIntegerField()
    bank_id = models.IntegerField()
    transaction_gateway_id = models.CharField(max_length=8)

    objects = CopyManager()
class DatasetGenerate(models.Model):
    time_internal = models.DateTimeField(primary_key=True, default=timezone.now, editable=False)
    count = models.IntegerField()
    dest_wallet_id = models.BigIntegerField()
    transaction_type = models.IntegerField()
    # transaction_type_chain = ArrayField(models.CharField(max_length=128), blank=True)
    transaction_type_chain = models.CharField(max_length=128)
    wallet_nickname = models.CharField(max_length=16, null=True, blank=True)
    transaction_cost = models.BigIntegerField()
    transaction_value = models.BigIntegerField()
    bank_id = models.IntegerField()
    transaction_gateway_id = models.CharField(max_length=8)
    #retention_time = models.DateTimeField(default=timezone.now)

    objects = CopyManager()

class DatasetBackup1(models.Model):
    time_internal = models.DateTimeField(primary_key=True, default=None)
    count = models.IntegerField()
    dest_wallet_id = models.BigIntegerField()
    transaction_type = models.IntegerField()
    wallet_nickname = models.CharField(max_length=16, null=True, blank=True)
    transaction_cost = models.BigIntegerField()
    transaction_value = models.BigIntegerField()

    objects = CopyManager()

class DatasetBackup2(models.Model):
    time_internal = models.DateTimeField(primary_key=True, default=None)
    count = models.IntegerField(default=None)
    dest_wallet_id = models.BigIntegerField()
    transaction_type = models.IntegerField()
    wallet_nickname = models.CharField(max_length=16, null=True, blank=True)
    transaction_cost = models.BigIntegerField()
    transaction_value = models.BigIntegerField()

    objects = CopyManager()