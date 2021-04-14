import csv
import os
import datetime
from django.core.management.base import BaseCommand, CommandError
from squirrel.models import biaoge

class Command(BaseCommand):
    help = 'Export as a csv file'
    def add_arguments(self,parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        with open(options['file'],'w') as k:
            writer = csv.DictWriter(
                    k, 
                    fieldnames = ['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color',
                        'Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging',
                        'Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches',
                        'Indifferent','Runs from']
                    )
            writer.writeheader()
            for item in biaoge.objects.all():
                if item.date: 
                    date_form = item.date.strftime('%m%d%Y')
                else:
                    date_form = item.date

                writer.writeitem({
                    'X': item.xx,
                    'Y': item.yy,
                    'Unique Squirrel ID': item.Unique_Squirrel_ID,
                    'Shift': item.shift,
                    'Date': date_form,
                    'Age': item.age,
                    'Primary Fur Color': item.primary_fur_color,
                    'Location': item.location,
                    'Specific Location': item.specific_location,
                    'Running': item.running,
                    'Chasing': item.chasing,
                    'Climbing': item.climbing,
                    'Eating': item.eating,
                    'Foraging': item.foraging,
                    'Other Activities': item.other_activities,
                    'Kuks': item.kuks,
                    'Quaas': item.quaas,
                    'Moans': item.moans,
                    'Tail flags': item.tail_flags,
                    'Tail twitches': item.tail_twitches,
                    'Approaches': item.approaches,
                    'Indifferent': item.indifferent,
                    'Runs from': item.runs_from,
                    })
            print('Successfully Exported the Data')