import csv
import os
import datetime
from django.core.management.base import BaseCommand, CommandError
from squirrel.models import biaoge


class Command(BaseCommand):
    help = 'Import the csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self,*args,**options):
        def trans_text(text):
            text_1 = text.upper()
            if text_1 == 'false':
                return False
            elif text_1 == 'true':
                return True
            else:
                return None

        with open(options['csv_file'], 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                alldata = biaoge()
                alldata.xx = float(row['X'])
                alldata.yy = float(row['Y'])
                alldata.Unique_Squirrel_ID = row['Unique Squirrel ID']
                alldata.shift = row['Shift']
                alldata.date = datetime.datetime.strptime(row['Date'],'%m%d%Y')
                alldata.age = row['Age']
                alldata.primary_fur_color = row['Primary Fur Color']
                alldata.location = row['Location']
                alldata.specific_location = row['Specific Location']
                alldata.foraging = trans_text(row['Foraging'])
                alldata.eating = trans_text(row['Eating'])
                alldata.climbing = trans_text(row['Climbing'])
                alldata.chasing = trans_text(row['Chasing'])
                alldata.running = trans_text(row['Running'])
                alldata.other_activities = row['Other Activities']
                alldata.kuks = trans_text(row['Kuks'])
                alldata.quaas = trans_text(row['Quaas'])
                alldata.moans = trans_text(row['Moans'])
                alldata.tail_flags = trans_text(row['Tail flags'])
                alldata.tail_twitches = trans_text(row['Tail twitches'])
                alldata.approaches = trans_text(row['Approaches'])
                alldata.indifferent = trans_text(row['Indifferent'])
                alldata.runs_from = trans_text(row['Runs from'])            
                alldata.save()
            print('Successfully imported the data')