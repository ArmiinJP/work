from django.core.management.base import BaseCommand
from crontab import CronTab


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        my_cron = CronTab(user='arminjp')
        job = my_cron.new(command='cd /home/arminjp/Documents/Project/generator/ && /home/arminjp/Documents/Project/generator/.venv/bin/python /home/arminjp/Documents/Project/generator/manage.py generate_data > /tmp/cronlog.txt 2>&1')
        job.minute.every(3)
        my_cron.write()
        for job in my_cron:
            print(job)